#web.py中db实现数据的批量插入

在SQL中，实现数据的批量插入，类型如：

    insert into tablename (filed1,field2) values (a1,a2),(b1,b2)

在web.py框架中，实现数据批量插入的方法是：

    multiple_insert(self, tablename, values, seqname=None, _test=False)

Inserts multiple rows into tablename. The values must be a list of dictioanries, one for each row to be inserted, each with the same set of keys. Returns the list of ids of the inserted rows.

Set seqname to the ID if it's not the default, or to False if there isn't one.

    >>> db = DB(None, {})

    >>> db.supports_multiple_insert = True

    >>> values = [{"name": "foo", "email": "foo@example.com"}, {"name": "bar", "email": "bar@example.com"}]

    >>> db.multiple_insert('person', values=values, _test=True)

    <sql: "INSERT INTO person (name, email) VALUES ('foo', 'foo@example.com'), ('bar', 'bar@example.com')">

var:http://webpy.org/docs/0.3/api#web.db

