import rethinkdb
# None r
rethinkdb.__doc__ = u'The toplevel RQL namespace.\n\nSetup your top level namespace.\n>>> import rethinkdb as r'
# r connect
rethinkdb.connect.__doc__ = u"Create a new connection to the database server.<br /><br />If the\nconnection cannot be established, a <code>RqlDriverError</code> exception will\nbe thrown.\n\n\nOpens a connection using the default host and port but specifying the default database.\n>>> conn = r.connect(db='heroes')"
# connection repl
rethinkdb.net.Connection.repl.__func__.__doc__ = u"Set the default connection to make REPL use easier. Allows calling\n<code>run()</code> without specifying a connection. <br/><br />\nConnection objects are not thread safe and <code>repl</code> connections\nshould not be used in multi-threaded environments.\n\n\nSet the default connection in REPL, and call `run()`\nwithout specifying the connection.\n\n>>> r.connect().repl()\nr.table('users').run()\n"
# connection close
rethinkdb.net.Connection.close.__func__.__doc__ = u'Close an open connection. Closing a connection cancels all outstanding\nrequests and frees the memory associated with the open requests.\n\n\nClose an open connection.\n>>> conn.close()'
# connection reconnect
rethinkdb.net.Connection.reconnect.__func__.__doc__ = u'Close and attempt to reopen a connection. Has the effect of canceling\nany outstanding request while keeping the connection open.\n\n\nCancel outstanding requests/queries that are no longer needed.\n>>> conn.reconnect()'
# connection use
rethinkdb.net.Connection.use.__func__.__doc__ = u"Change the default database on this connection.\n\nChange the default database so that we don't need\nto specify the database when referencing a table.\n\n>>> conn.use('heroes')"
# query run
rethinkdb.ast.RqlQuery.run.__func__.__doc__ = u"Run a query on a connection.\n\nCall run on the connection with a query to execute the query.\nThe callback will get a cursor from which results may be retrieved.\n\n>>> for doc in r.table('marvel').run(conn):\n  print doc\n\n\nIf you are OK with potentially out of date data from all the tables\ninvolved in this query and want potentially faster reads, pass a flag\nallowing out of date data in an options object.  Settings for\nindividual tables will supercede this global setting for all tables\nin the query.\n\n>>> r.table('marvel').run(conn, use_outdated=True)\n\nIf you just want to send a write and forget about it, you\ncan set `noreply` to true in the options.  In this case\n`run` will return immediately.\n\n>>> r.table('marvel').run(conn, noreply=True)"
# cursor next
# cursor hasNext
# cursor each
# cursor toArray
# r db_create
rethinkdb.db_create.__doc__ = u"Create a database. A RethinkDB database is a collection of tables,\nsimilar to relational databases.<br /><br />If successful, the operation returns\nan object: <code>{created: 1}</code>. If a database with the same name already\nexists the operation throws <code>RqlRuntimeError</code>.\n\n\nCreate a database named 'superheroes'.\n>>> r.db_create('superheroes').run(conn)"
# r db_drop
rethinkdb.db_drop.__doc__ = u"Drop a database. The database, all its tables, and corresponding\ndata will be deleted.<br /><br />If successful, the operation returns the object\n<code>{dropped: 1}</code>. If the specified database doesn't exist a <code>RqlRuntimeError</code>\nis thrown.\n\n\nDrop a database named 'superheroes'.\n>>> r.db_drop('superheroes').run(conn)"
# r db_list
rethinkdb.db_list.__doc__ = u'List all database names in the system.<br /><br />\nThe result is a list of strings.\n\n\nList all databases.\n>>> r.db_list().run(conn)'
# db table_create
rethinkdb.ast.DB.table_create.__func__.__doc__ = u"Create a table. A RethinkDB table is a collection of JSON documents.\n<br /><br />If successful, the operation returns an object: <code>{created: 1}</code>.  If\na table with the same name already exists, the operation throws <code>RqlRuntimeError</code>.\n<br /><br />When creating a table you can specify the following options:\n<ul>\n<li><code>primary_key</code>(string): the name of the primary key. The default primary key is <code>id</code>;</li>\n<li><code>hard_durability</code>(boolean): if set to <code>false</code>, this enables <strong>soft durability</strong>\n on this table: writes will be acknowledged by the server immediately and flushed to disk in the background. \n Default is <code>true</code> (hard durability);</li>\n<li><code>cache_size</code>(number): set the cache size (in MB) to be used by the table. Default is 1024MB;</li>\n<li><code>datacenter</code>(string): the name of the datacenter this table should be assigned to.</li>\n</ul>\n<br /><br />In Javascript, these options can use either the underscore or camelcase form (e.g. primaryKey, hardDurability).\n\n\nCreate a table named 'dc_universe' with the primary key set to field 'id'.\nIf a new document doesn't contain the field 'id', the database will\nautogenerate a value for it.\n\n>>> r.db('test').table_create('dc_universe').run(conn)\n\nCreate a table named 'dc_universe' using the field 'name'\nas primary key.\n\n>>> r.db('test').table_create('dc_universe', primary_key='name').run(conn)\n\nCreate a table to log the very fast actions of the heroes.\n\n>>> r.db('test').table_create('hero_actions', hard_durability=False).run(conn)"
# db table_drop
rethinkdb.ast.DB.table_drop.__func__.__doc__ = u"Drop a table. The table and all its data will be deleted.<br /><br\n/>If succesful, the operation returns an object: <code>{dropped: 1}</code>.\nIf the specified table doesn''t exist a <code>RqlRuntimeError</code> is thrown.\n\n\nDrop a table named 'dc_universe'.\n>>> r.db('test').table_drop('dc_universe').run(conn)"
# db table_list
rethinkdb.ast.DB.table_list.__func__.__doc__ = u"List all table names in a database.<br /><br />\nThe result is a list of strings.\n\n\nList all tables of the 'test' database.\n>>> r.db('test').table_list().run(conn)"
# table index_create
rethinkdb.ast.Table.index_create.__func__.__doc__ = u"Create a new secondary index on this table.\n\nTo efficiently query our heros by name we can create a secondary\nindex based on the value of that field. We can already quickly query\nheros by name with the primary index but to do the same based on hero\ncode names we'll have to create a secondary index based on that\nattribute.\n\n>>> r.table('dc').index_create('code_name').run(conn)\n\nYou can also create a secondary index based on an arbitrary function\non the document.\n\n>>> r.table('dc').index_create('power_rating',\n  lambda hero: hero['combat_power'] + (2 * hero['compassion_power'])\n).run(conn)\n\n\nA compound index can be created by returning an array of values to\nuse as the secondary index key.\n\n>>> r.table('dc').index_create('parental_planets',\n  lambda hero: [hero['mothers_home_planet'], hero['fathers_home_planet']]\n).run(conn)\n"
# table index_drop
rethinkdb.ast.Table.index_drop.__func__.__doc__ = u"Delete a previously created secondary index of this table.\n\nDrop a secondary index named 'code_name'.\n>>> r.table('dc').index_drop('code_name').run(conn)"
# table index_list
rethinkdb.ast.Table.index_list.__func__.__doc__ = u"List all the secondary indexes of this table.\n\nList the available secondary indexes for this table.\n>>> r.table('marvel').index_list()"
# table insert
rethinkdb.ast.Table.insert.__func__.__doc__ = u"Insert JSON documents into a table. Accepts a single JSON document\nor an array of documents. <br /><br />\nInsert returns an object that contains the following attributes:\n<ul>\n<li><code>inserted</code> - the number of documents that were succesfully inserted;</li>\n<li><code>replaced</code> - the number of documents that were updated when <code>upsert</code> is used;</li>\n<li><code>unchanged</code> - the number of documents that would have been modified, except that the new\nvalue was the same as the old value when doing an <code>upsert</code>;</li>\n<li><code>errors</code> - the number of errors encountered while inserting;</li>\n<li>if errors where encountered while inserting, <code>first_error</code> contains the text of the first error;</li>\n<li><code>generated_keys</code> - a list of generated primary key values;</li>\n<li><code>deleted</code> and <code>skipped</code> \n- <code>0</code> for an <code>insert</code> operation.</li>\n</ul>\n\n\nInsert a row into a table named 'marvel'.\n>>> r.table('marvel').insert(\n    { 'superhero': 'Iron Man', 'superpower':'Arc Reactor' }).run(conn)\n\n\nInsert multiple rows into a table named 'marvel'.\n>>> r.table('marvel').insert([\n  { 'superhero': 'Wolverine', 'superpower': 'Adamantium' },\n  { 'superhero': 'Spiderman', 'superpower': 'spidy sense' }\n]).run(conn)\n\n\nInsert a row into a table named 'marvel', overwriting if the document already exists.\n>>> r.table('marvel').insert(\n  { 'superhero': 'Iron Man', 'superpower': 'Arc Reactor' },\n  upsert=True\n).run(conn)\n"
# selection update
rethinkdb.ast.RqlQuery.update.__func__.__doc__ = u"Update JSON documents in a table. Accepts a JSON document, a RQL\nexpression, or a combination of the two.<br /><br />\nUpdate returns an object that contains the following attributes:\n<ul>\n<li><code>replaced</code> - the number of documents that were updated;</li>\n<li><code>unchanged</code> - the number of documents that would have been modified  \nexcept the new value was the same as the old value;</li>\n<li><code>skipped</code> - the number of documents that were left unmodified because\nthere was nothing to do: either the row didn't exist or the new value is null;</li>  \n<li><code>errors</code> - the number of errors encountered while performing the update;</li>\n<li>if errors occured, <code>first_error</code> contains the text of the first error;</li>\n<li><code>deleted</code> and  <code>inserted</code> \n- <code>0</code> for an <code>update</code> operation.</li>\n</ul>\n\n\nUpdate Superman's age to 30. If attribute 'age' doesn't\nexist, adds it to the document.\n\n>>> r.table('marvel').get('superman').update({ 'age': 30 }).run(conn)\n\nIncrement every superhero's age. If age doesn't exist, throws an error.\n\n>>> r.table('marvel').update(lambda x: {'age': x['age'] + 1}).run(conn)\n\nAllow the server to run non-atomic operations.\n>>> r.table('marvel').update(\n    lambda x: {'age': x['age'] + r.js('1')}, non_atomic=True).run(conn)\n"
# selection replace
rethinkdb.ast.RqlQuery.replace.__func__.__doc__ = u"Replace documents in a table. Accepts a JSON document or a RQL expression,\nand replaces the original document with the new one. The new document must have\nthe same primary key as the original document.<br /><br />\nReplace returns an object that contains the following attributes:\n<ul>\n<li><code>replaced</code> - the number of documents that were replaced;</li>\n<li><code>unchanged</code> - the number of documents that would have been modified,\nexcept that the new value was the same as the old value;</li>\n<li><code>inserted</code> - the number of new documents added. You can have new documents\ninserted if you do a point-replace on a key that isn't in the table or you do a replace\non a selection and one of the documents you are replacing has been deleted;</li>\n<li><code>deleted</code> - the number of deleted documents when doing a replace with null;</li>\n<li><code>errors</code> - the number of errors encountered while performing the replace;</li>\n<li>if errors occurred performing the replace, <code>first_error</code> contains the text of the first error encountered;</li>\n<li><code>skipped</code> - <code>0</code> for a <code>replace</code> operation.</li>\n</ul>\n\n\nRemove all existing attributes from Superman's document, and add an attribute 'age'.\n>>> r.table('marvel').get('superman').replace({ 'id': 'superman', 'age': 30 }).run(conn)\n\nAllow the server to run non-atomic operations.\n>>> r.table('marvel').get('superman').replace(\n    { 'id': 'superman', 'age': 30 }, non_atomic=True).run(conn)\n\n\nMark all Marvel heroes as favorites.\n>>> r.table('heroes').filter(r.row['universe'] == 'marvel').replace(\n    lambda hero: hero.merge({'is_fav': True})).run(conn)\n"
# selection delete
rethinkdb.ast.RqlQuery.delete.__func__.__doc__ = u"Delete one or more documents from a table.<br /><br />\nDelete returns an object that contains the following attributes:\n<ul>\n<li><code>deleted</code> - the number of documents that were deleted;</li>\n<li><code>skipped</code> - the number of documents from the selection that were left unmodified \nbecause there was nothing to do. For example, if you delete a row that has already been deleted, \nthat row will be skipped;</li>\n<li><code>errors</code> - the number of errors encountered while deleting;</li>\n<li>if errors occured, <code>first_error</code> contains the text of the first error;</li>\n<li><code>inserted</code>, <code>replaced</code>, and <code>unchanged</code> - all \n<code>0</code> for a <code>delete</code> operation.</li>\n</ul>\n\n\nDelete superman from the database.\n>>> r.table('marvel').get('superman').delete().run(conn)\n\nDelete every document from the table 'marvel'.\n>>> r.table('marvel').delete().run(conn)"
# r db
rethinkdb.db.__doc__ = u"Reference a database.\n\nBefore we can query a table we have to select the correct database.\n>>> r.db('heroes').table('marvel').run(conn)"
# db table
rethinkdb.ast.DB.table.__func__.__doc__ = u"Select all documents in a table. This command can be chained with\nother commands to do further processing on the data.\n\n\nReturn all documents in the table 'marvel' of the default database.\n>>> r.table('marvel').run(conn)\n\nReturn all documents in the table 'marvel' of the database 'heroes'.\n>>> r.db('heroes').table('marvel').run(conn)\n\nIf you are OK with potentially out of date data\nfrom this table and want potentially faster reads, pass\na flag allowing out of date data.\n\n>>> r.db('heroes').table('marvel', True).run(conn)"
# table get
rethinkdb.ast.Table.get.__func__.__doc__ = u"Get a document by primary key.\n\nFind a document with the primary key 'superman'.\n>>> r.table('marvel').get('superman').run(conn)"
# table get_all
rethinkdb.ast.Table.get_all.__func__.__doc__ = u'Get all documents where the given value matches the value of the requested index.\n\nSecondary index keys are not guaranteed to be unique so we cannot\nquery via "get" when using a secondary index.\n\n>>> r.table(\'marvel\').get_all(\'man_of_steel\', index=\'code_name\').run(conn)\n\nWithout an index argument, we default to the primary index. While\n`get` will either return the document or `null` when no document\nwith such a primary key value exists, this will return either a one\nor zero length stream.\n\n>>> r.table(\'dc\').get_all(\'superman\').run(conn)'
# selection between
rethinkdb.ast.RqlQuery.between.__func__.__doc__ = u"Get all documents between two primary keys (both keys are inclusive).\n\nFind all users with primary keys between 10 and 20, inclusive.\n>>> r.table('marvel').between(10, 20).run(conn)\n\nBetween can be used on secondary indexes too. Just pass an optional index\nargument giving the secondary index to query.\n\n>>> r.table('dc').between('dark_knight', 'man_of_steel', index='code_name').run(conn)"
# selection filter
rethinkdb.ast.RqlQuery.filter.__func__.__doc__ = u"Get all the documents for which the given predicate is true.<br /><br />\n<code>filter</code> can be called on a sequence, selection, or a\nfield containing an array of elements. The return type is the\nsame as the type on which the function was called on.\n\n\nGet all active users aged 30.\n>>> r.table('users').filter({'active': True, 'age': 30}).run(conn)\n\nSelect all documents where the 'magazines' field is greater than 5.\n>>> r.table('users').filter(r.row['magazines'] > 5).run(conn)\n\nSelect all documents where the 'abilities' embedded document has an attribute called 'super-strength'.\n>>> r.table('marvel').filter(\n    lambda hero: hero['abilities'].contains('super-strength')).run(conn)\n\n\nSelect all documents where the field 'powers' containing an array has an element equal to 10.\n>>> r.table('marvel').filter(\n  r.row['powers'].filter(lambda el: el == 10).count() > 0\n).run(conn)\n"
# sequence inner
# sequence outer
# sequence eqJoin
rethinkdb.ast.RqlQuery.eq_join.__func__.__doc__ = u"An efficient join that looks up elements in the right table by primary key.\n\nLet our heroes join forces to battle evil!\n>>> r.table('marvel').eq_join('main_dc_collaborator', r.table('dc')).run(conn)\n\nThe above query is equivalent to this inner join but runs in O(n log(m)) time rather than the O(n * m) time the inner join takes.\n>>> r.table('marvel').inner_join(r.table('dc'),\n  lambda left, right: left['main_dc_collaborator'] == right['hero_name']).run(conn)\n\nYou can take advantage of a secondary index on the second table by giving an optional index parameter.\n>>> r.table('marvel').eq_join('main_weapon_origin',\n    r.table('mythical_weapons'), index='origin').run(conn)\n"
# sequence zip
rethinkdb.ast.RqlQuery.zip.__func__.__doc__ = u"Used to 'zip' up the result of a join by merging the 'right' fields into 'left' fields of each member of the sequence.\n\n'zips up' the sequence by merging the left and right fields produced by a join.\n>>> r.table('marvel').eq_join('main_dc_collaborator', r.table('dc')).zip().run(conn)"
# sequence map
rethinkdb.ast.RqlQuery.map.__func__.__doc__ = u"Transform each element of the sequence by applying the given mapping function.\n\nConstruct a sequence of hero power ratings.\n>>> r.table('marvel').map(\n    lambda hero: hero['combatPower'] + hero['compassionPower'] * 2).run(conn)"
# sequence concat_map
rethinkdb.ast.RqlQuery.concat_map.__func__.__doc__ = u"Flattens a sequence of arrays returned by the <code>mappingFunction</code> into a single sequence.\n\nConstruct a sequence of all monsters defeated by Marvel heroes. Here the field 'defeatedMonsters' is a list that is concatenated to the sequence.\n>>> r.table('marvel').concat_map(lambda hero: hero['defeatedMonsters']).run(conn)"
# sequence order_by
rethinkdb.ast.RqlQuery.order_by.__func__.__doc__ = u"Sort the sequence by document values of the given key(s).<br /><br /> <code>order by</code> defaults to ascending ordering. To explicitly specify the ordering, wrap the attribute with either <code>r.asc</code> or <code>r.desc</code>.\n\nOrder our heroes by a series of performance metrics.\n>>> r.table('marvel').order_by('enemies_vanquished', 'damsels_saved').run(conn)\n\nLet's lead with our best vanquishers by specify descending ordering.\n>>> r.table('marvel').order_by(\n    r.desc('enemies_vanquished'), r.asc('damsels_saved')).run(conn)"
# sequence skip
rethinkdb.ast.RqlQuery.skip.__func__.__doc__ = u"Skip a number of elements from the head of the sequence.\n\nHere in conjunction with `order_by` we choose to ignore the most successful heroes.\n>>> r.table('marvel').order_by('successMetric').skip(10).run(conn)"
# sequence limit
rethinkdb.ast.RqlQuery.limit.__func__.__doc__ = u"End the sequence after the given number of elements.\n\nOnly so many can fit in our Pantheon of heroes.\n>>> r.table('marvel').order_by('belovedness').limit(10).run(conn)"
# sequence slice
rethinkdb.ast.RqlQuery.slice.__func__.__doc__ = u"Trim the sequence to within the bounds provided.\n\nFor this fight, we need heroes with a good mix of strength and agility.\n>>> r.table('marvel').order_by('strength')[5:10].run(conn)"
# sequence nth
rethinkdb.ast.RqlQuery.nth.__func__.__doc__ = u'Get the nth element of a sequence.\n\nSelect the second element in the array.\n>>> r.expr([1,2,3])[1].run(conn)'
# sequence union
rethinkdb.ast.RqlQuery.union.__func__.__doc__ = u"Concatenate two sequences.\n\nConstruct a stream of all heroes.\n>>> r.table('marvel').union(r.table('dc')).run(conn)"
# sequence reduce
rethinkdb.ast.RqlQuery.reduce.__func__.__doc__ = u"Produce a single value from a sequence through repeated application\nof a reduction function.<br /><br />\nThe <code>reduce</code> function gets invoked repeatedly not only \nfor the input values but also for results of previous reduce invocations. \nThe type and format of the object that is passed in to reduce must be \nthe same with the one returned from reduce.\n\n\nHow many enemies have our heroes defeated?\n>>> r.table('marvel').map(r.row['monsters_killed']).reduce(\n    lambda acc, val: acc + val, 0).run(conn)"
# sequence count
# sequence distinct
rethinkdb.ast.RqlQuery.distinct.__func__.__doc__ = u"Remove duplicate elements from the sequence.\n\nWhich unique villains have been vanquished by marvel heroes?\n>>> r.table('marvel').concat_map(lambda hero: hero['villainList']).distinct().run(conn)"
# sequence groupedmapreduce
rethinkdb.ast.RqlQuery.grouped_map_reduce.__func__.__doc__ = u"Partition the sequence into groups based on the <code>grouping</code> function. The elements of each group are then mapped using the <code>mapping</code> function and reduced using the <code>reduction</code> function.<br /><br /><code>grouped_map_reduce</code> is a generalized form of <code>group by</code>.\n\nIt's only fair that heroes be compared against their weight class.\n>>> r.table('marvel').grouped_map_reduce(\n  lambda hero: hero['weightClass'],  # grouping\n  lambda hero: hero.pluck('name', 'strength'),  # mapping\n  lambda acc, hero: r.branch(acc['strength'] < hero['strength'], hero, acc),\n  {'name':'none', 'strength':0}  # base\n).run(conn)"
# sequence group_by
rethinkdb.ast.RqlQuery.group_by.__func__.__doc__ = u"Groups elements by the values of the given attributes and then applies the given reduction. Though similar to <code>grouped_map_reduce</code>, groupby takes a standardized object for specifying the reduction. Can be used with a number of predefined common reductions.\n\nUsing a predefined reduction we can easily find the average strength of members of each weight class.\n>>> r.table('marvel').group_by('weightClass', r.avg('strength')).run(conn)"
# r count
# r sum
rethinkdb.sum.__doc__ = u"Compute the sum of the given field in the group.\n\nHow many enemies have been vanquished by heroes at each strength level?\n>>> r.table('marvel').group_by('strength', r.sum('enemiesVanquished')).run(conn)"
# r avg
rethinkdb.avg.__doc__ = u"Compute the average value of the given attribute for the group.\n\nWhat's the average agility of heroes at each strength level?\n>>> r.table('marvel').group_by('strength', r.avg('agility')).run(conn)"
# r row
rethinkdb.row.__doc__ = u"Returns the currently visited document.\n\nGet all users whose age is greater than 5.\n>>> r.table('users').filter(r.row['age'] > 5).run(conn)\n\nAccessing the attribute 'child' of an embedded document.\n>>> r.table('users').filter(r.row['embedded_doc']['child'] > 5).run(conn)\n\nAdd 1 to every element of an array.\n>>> r.expr([1, 2, 3]).map(r.row + 1).run(conn)\n\nFor nested queries functions should be used instead of r.row.\n>>> r.table('users').filter(\n    lambda doc: doc['name'] == r.table('prizes').get('winner')).run(conn)"
# sequence pluck
rethinkdb.ast.RqlQuery.pluck.__func__.__doc__ = u"Plucks out one or more attributes from either an object or a sequence of objects (projection).\n\nWe just need information about IronMan's reactor and not the rest of the document.\n>>> r.table('marvel').get('IronMan').pluck('reactorState', 'reactorPower').run(conn)\n\nFor the hero beauty contest we only care about certain qualities.\n>>> r.table('marvel').pluck('beauty', 'muscleTone', 'charm').run(conn)"
# sequence without
rethinkdb.ast.RqlQuery.without.__func__.__doc__ = u"The opposite of pluck; takes an object or a sequence of objects, and removes all attributes except for the ones specified.\n\nSince we don't need it for this computation we'll save bandwidth and leave out the list of IronMan's romantic conquests.\n>>> r.table('marvel').get('IronMan').without('personalVictoriesList').run(conn)\n\nWithout their prized weapons, our enemies will quickly be vanquished.\n>>> r.table('enemies').without('weapons').run(conn)"
# json merge
rethinkdb.ast.RqlQuery.merge.__func__.__doc__ = u"Merge two objects together to construct a new object with properties from both. Gives preference to attributes from other when there is a conflict.\n\nEquip IronMan for battle.\n>>> r.table('marvel').get('IronMan').merge(\n  r.table('loadouts').get('alienInvasionKit')).run(conn)"
# json append
rethinkdb.ast.RqlQuery.append.__func__.__doc__ = u"Append a value to an array.\n\nRetrieve Iron Man's equipment list with the addition of some new boots.\n>>> r.table('marvel').get('IronMan')['equipment'].append('newBoots').run(conn)"
# json getattr
# json contains
rethinkdb.ast.RqlQuery.contains.__func__.__doc__ = u"Test if an object has the given attribute. <br /><br /> <code>contains</code> can only be called on objects and not on <code>string</code> or <code>array</code> attributes.\n\nWhich heroes are married?\n>>> r.table('marvel').filter(lambda hero: hero.contains('spouse')).run(conn)"
# number | string add
rethinkdb.ast.RqlQuery.add.__func__.__doc__ = u'Sum two numbers or concatenate two strings.\n\nIt\'s as easy as 2 + 2 = 4.\n>>> (r.expr(2) + 2).run(conn)\n\nStrings can be concatenated too.\n>>> (r.expr("foo") + "bar").run(conn)'
# number sub
rethinkdb.ast.RqlQuery.sub.__func__.__doc__ = u"Subtract two numbers.\n\nIt's as easy as 2 - 2 = 0.\n>>> (r.expr(2) - 2).run(conn)"
# number mul
rethinkdb.ast.RqlQuery.mul.__func__.__doc__ = u"Multiply two numbers.\n\nIt's as easy as 2 * 2 = 4.\n>>> (r.expr(2) * 2).run(conn)"
# number div
rethinkdb.ast.RqlQuery.div.__func__.__doc__ = u"Divide two numbers.\n\nIt's as easy as 2 / 2 = 1.\n>>> (r.expr(2) / 2).run(conn)"
# number mod
rethinkdb.ast.RqlQuery.mod.__func__.__doc__ = u"Find the remainder when dividing two numbers.\n\nIt's as easy as 2 % 2 = 0.\n>>> (r.expr(2) % 2).run(conn)"
# bool and
rethinkdb.ast.RqlQuery.__and__.__func__.__doc__ = u'Compute the logical and of two values.\n\nTrue and false anded is false?\n>>> (r.expr(True) & False).run(conn)'
# bool or
rethinkdb.ast.RqlQuery.__or__.__func__.__doc__ = u'Compute the logical or of two values.\n\nTrue or false ored is true?\n>>> (r.expr(True) | False).run(conn)'
# json eq
rethinkdb.ast.RqlQuery.eq.__func__.__doc__ = u'Test if two values are equal.\n\nDoes 2 equal 2?\n>>> (r.expr(2) == 2).run(conn)'
# json ne
rethinkdb.ast.RqlQuery.ne.__func__.__doc__ = u'Test if two values are not equal.\n\nDoes 2 not equal 2?\n>>> (r.expr(2) != 2).run(conn)'
# json gt
rethinkdb.ast.RqlQuery.gt.__func__.__doc__ = u'Test if the first value is greater than other.\n\nIs 2 greater than 2?\n>>> (r.expr(2) > 2).run(conn)'
# json ge
rethinkdb.ast.RqlQuery.ge.__func__.__doc__ = u'Test if the first value is greater than or equal to other.\n\nIs 2 greater than or equal to 2?\n>>> (r.expr(2) >= 2).run(conn)'
# json lt
rethinkdb.ast.RqlQuery.lt.__func__.__doc__ = u'Test if the first value is less than other.\n\nIs 2 less than 2?\n>>> (r.expr(2) < 2).run(conn)'
# json le
rethinkdb.ast.RqlQuery.le.__func__.__doc__ = u'Test if the first value is less than or equal to other.\n\nIs 2 less than or equal to 2?\n>>> (r.expr(2) <= 2).run(conn)'
# bool not
# r do
rethinkdb.do.__doc__ = u"Evaluate the <code>inExpr</code> in the context of one or more value\nbindings.<br /><br />\nThe type of the result is the type of the value returned from <code>inExpr</code>.\n\n\nThe object(s) passed to do() can be bound to name(s). The last argument is the expression to evaluate in the context of the bindings.\n>>> r.do(r.table('marvel').get('IronMan'),\n     lambda ironman: ironman['name']).run(conn)"
# r branch
rethinkdb.branch.__doc__ = u"Evaluate one of two control paths based on the value of an expression. \n<code>branch</code> is effectively an <code>if</code> renamed due to\nlanguage constraints.<br /><br />\nThe type of the result is determined by the type of the branch that\ngets executed.\n\n\nReturn the manlier of two heroes:\n>>> r.table('marvel').map(r.branch(r.row['victories'] > 100,\n    r.row['name'] + ' is a superhero',\n    r.row['name'] + ' is a hero')\n).run(conn)"
# r foreach
# r error
rethinkdb.error.__doc__ = u"Throw a runtime error.\n\nIron Man can't possibly have lost a battle:\n>>> r.table('marvel').get('IronMan').do(\n  lambda ironman: r.branch(ironman['victories'] < ironman['battles'],\n                            r.error('impossible code path'),\n                            ironman)\n).run(conn)"
# r expr
rethinkdb.expr.__doc__ = u"Construct a RQL JSON object from a native object.\n\nObjects wrapped with expr can then be manipulated by RQL API functions.\n>>> r.expr({'a':'b'}).merge({'b':[1,2,3]}).run(conn)"
# r js
rethinkdb.js.__doc__ = u'Create a javascript expression.\n\nConcatenate two strings using Javascript\'\n>>> r.js("\'str1\' + \'str2\'").run(conn)\n\nSelect all documents where the \'magazines\' field is greater than 5 by running Javascript on the server.\n>>> r.table(\'marvel\').filter(\n  r.js(\'(function (row) { return row.magazines > 5; })\')).run(conn)\n\nYou may also specify a timeout in seconds (defaults to 5).\n>>> r.js(\'while(true) {}\', timeout=1.3).run(conn)'
# json coerce_to
rethinkdb.ast.RqlQuery.coerce_to.__func__.__doc__ = u"Converts a value of one type into another. <br /><br />\nYou can convert: a selection, sequence, or object into an ARRAY, \nan array of pairs into an OBJECT, and any DATUM into a STRING.\n\n\nConvert a table to an array.\n>>> r.table('marvel').coerce_to('array').run(conn)\n\nConvert an array of pairs into an object.\n>>> r.expr([['name', 'Ironman'], ['victories', 2000]]).coerce_to('object').run(conn)\n\nConvert a number to a string.\n>>> r.expr(1).coerce_to('string').run(conn)"
# value type_of
rethinkdb.ast.RqlQuery.type_of.__func__.__doc__ = u'Gets the type of a value.\n\nGet the type of a string.\n>>> r.expr("foo").type_of().run(conn)'
# value info
rethinkdb.ast.RqlQuery.info.__func__.__doc__ = u"Get information about a RQL value.\n\nGet information about a table such as primary key, or cache size.\n\n>>> r.table('marvel').info().run(conn)"