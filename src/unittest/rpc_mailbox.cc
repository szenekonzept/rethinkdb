#include "unittest/gtest.hpp"

#include "arch/timing.hpp"
#include "rpc/mailbox/mailbox.hpp"
#include "rpc/mailbox/typed.hpp"
#include "unittest/unittest_utils.hpp"

namespace unittest {

namespace {

/* `dummy_mailbox_t` is a `raw_mailbox_t` that keeps track of messages it receives.
You can send to a `dummy_mailbox_t` with `send()`. */

struct dummy_mailbox_t {
private:
    std::set<int> inbox;
    void on_message(read_stream_t *stream) {
        int i;
        int res = deserialize(stream, &i);
        if (res) { throw fake_archive_exc_t(); }
        inbox.insert(i);
    }
public:
    explicit dummy_mailbox_t(mailbox_manager_t *m) :
        mailbox(m, boost::bind(&dummy_mailbox_t::on_message, this, _1))
        { }
    void expect(int message) {
        EXPECT_EQ(1, inbox.count(message));
    }
    raw_mailbox_t mailbox;
};

void write_integer(int i, write_stream_t *stream) {
    write_message_t msg;
    int32_t i_32 = i;
    msg << i_32;
    int res = send_write_message(stream, &msg);
    if (res) { throw fake_archive_exc_t(); }
}

void send(mailbox_manager_t *c, raw_mailbox_t::address_t dest, int message) {
    send(c, dest, boost::bind(&write_integer, message, _1));
}

}   /* anonymous namespace */

/* `MailboxStartStop` creates and destroys some mailboxes. */

void run_mailbox_start_stop_test() {
    int port = randport();
    connectivity_cluster_t c;
    mailbox_manager_t m(&c);
    connectivity_cluster_t::run_t r(&c, port, &m);

    /* Make sure we can create a mailbox */
    dummy_mailbox_t mbox1(&m);

    /* Make sure we can create a mailbox on an arbitrary thread */
    on_thread_t thread_switcher(1);
    dummy_mailbox_t mbox2(&m);
}
TEST(RPCMailboxTest, MailboxStartStop) {
    run_in_thread_pool(&run_mailbox_start_stop_test, 2);
}

/* `MailboxMessage` sends messages to some mailboxes */

void run_mailbox_message_test() {
    int port = randport();
    connectivity_cluster_t c1, c2;
    mailbox_manager_t m1(&c1), m2(&c2);
    connectivity_cluster_t::run_t r1(&c1, port, &m1), r2(&c2, port+1, &m2);
    r1.join(c2.get_peer_address(c2.get_me()));
    let_stuff_happen();

    /* Create a mailbox and send it three messages */
    dummy_mailbox_t mbox(&m1);
    raw_mailbox_t::address_t address = mbox.mailbox.get_address();

    send(&m1, address, 88555);
    send(&m2, address, 3131);
    send(&m1, address, 7);

    let_stuff_happen();

    mbox.expect(88555);
    mbox.expect(3131);
    mbox.expect(7);
}
TEST(RPCMailboxTest, MailboxMessage) {
    run_in_thread_pool(&run_mailbox_message_test);
}

TEST(RPCMailboxTest, MailboxMessageMultiThread) {
    run_in_thread_pool(&run_mailbox_message_test, 3);
}

/* `DeadMailbox` sends a message to a defunct mailbox. The expected behavior is
for the message to be silently ignored. */

void run_dead_mailbox_test() {
    int port = randport();
    connectivity_cluster_t c1, c2;
    mailbox_manager_t m1(&c1), m2(&c2);
    connectivity_cluster_t::run_t r1(&c1, port, &m1), r2(&c2, port+1, &m2);

    /* Create a mailbox, take its address, then destroy it. */
    raw_mailbox_t::address_t address;
    {
        dummy_mailbox_t mbox(&m1);
        address = mbox.mailbox.get_address();
    }

    send(&m1, address, 12345);
    send(&m2, address, 78888);

    let_stuff_happen();
}
TEST(RPCMailboxTest, DeadMailbox) {
    run_in_thread_pool(&run_dead_mailbox_test);
}
TEST(RPCMailboxTest, DeadMailboxMultiThread) {
    run_in_thread_pool(&run_dead_mailbox_test, 3);
}
/* `MailboxAddressSemantics` makes sure that `raw_mailbox_t::address_t` behaves as
expected. */

void run_mailbox_address_semantics_test() {

    raw_mailbox_t::address_t nil_addr;
    EXPECT_TRUE(nil_addr.is_nil());

    int port = randport();
    connectivity_cluster_t c;
    mailbox_manager_t m(&c);
    connectivity_cluster_t::run_t r(&c, port, &m);

    dummy_mailbox_t mbox(&m);
    raw_mailbox_t::address_t mbox_addr = mbox.mailbox.get_address();
    EXPECT_FALSE(mbox_addr.is_nil());
    EXPECT_TRUE(mbox_addr.get_peer() == c.get_me());
}
TEST(RPCMailboxTest, MailboxAddressSemantics) {
    run_in_thread_pool(&run_mailbox_address_semantics_test);
}
TEST(RPCMailboxTest, MailboxAddressSemanticsMultiThread) {
    run_in_thread_pool(&run_mailbox_address_semantics_test, 3);
}

/* `TypedMailbox` makes sure that `mailbox_t<>` works. */

void run_typed_mailbox_test() {

    int port = randport();
    connectivity_cluster_t c;
    mailbox_manager_t m(&c);
    connectivity_cluster_t::run_t r(&c, port, &m);

    std::vector<std::string> inbox;
    mailbox_t<void(std::string)> mbox(&m, boost::bind(&std::vector<std::string>::push_back, &inbox, _1), mailbox_callback_mode_inline);

    mailbox_addr_t<void(std::string)> addr = mbox.get_address();

    send(&m, addr, std::string("foo"));
    send(&m, addr, std::string("bar"));
    send(&m, addr, std::string("baz"));

    let_stuff_happen();

    EXPECT_EQ(inbox.size(), 3);
    if (inbox.size() == 3) {
        EXPECT_EQ(inbox[0], "foo");
        EXPECT_EQ(inbox[1], "bar");
        EXPECT_EQ(inbox[2], "baz");
    }
}
TEST(RPCMailboxTest, TypedMailbox) {
    run_in_thread_pool(&run_typed_mailbox_test);
}
TEST(RPCMailboxTest, TypedMailboxMultiThread) {
    run_in_thread_pool(&run_typed_mailbox_test, 3);
}

}   /* namespace unittest */
