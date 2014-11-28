#mongodb数据导入导出以及备份恢复 

##数据导出 mongoexport

假设库里有一张user表(collection)，里面有2 条记录，我们要将它导出

    > use my_mongodb
    switched to db my_mongodb
    > db.user.find();
    { "_id" : ObjectId("4f81a4a1779282ca68fd8a5a"), "uid" : 2, "username" : "Jerry", "age" : 100 }
    { "_id" : ObjectId("4f844d1847d25a9ce5f120c4"), "uid" : 1, "username" : "Tom", "age" : 25 }
    >

###1 常用导出方法

    [root@localhost bin]# ./mongoexport -d my_mongodb -c user -o user.dat
    connected to: 127.0.0.1
    exported 2 records
    [root@localhost bin]# cat user.dat
    { "_id" : { "$oid" : "4f81a4a1779282ca68fd8a5a" }, "uid" : 2, "username" : "Jerry", "age" : 100 }
    { "_id" : { "$oid" : "4f844d1847d25a9ce5f120c4" }, "uid" : 1, "username" : "Tom", "age" : 25 }
    [root@localhost bin]#

参数说明:
- -d 指明使用的库, 本例中为” my_mongodb”
- -c 指明要导出的表(collection), 本例中为”user”
- -o 指明要导出到的文件名, 本例中为”user.dat”

从上面可以看到导出的方式使用的是JSON 的样式

###2 导出CSV格式的文件

    [root@localhost bin]# ./mongoexport -d my_mongodb -c user --csv -f uid,username,age -o
    user_csv.dat
    connected to: 127.0.0.1
    exported 2 records
    [root@localhost bin]# cat user_csv.dat
    uid,username,age
    2,"Jerry",100
    1,"Tom",25
    [root@localhost bin]#

参数说明:

- -csv 指要要导出为csv 格式
- -f 指明需要导出哪些例

更详细的用法可以 mongoexport –help 来查看

##数据导入mongoimport

在上例中我们讨论的是导出工具的使用，那么本节将讨论如何向表中导入数据

###1 导入JSON 数据

我们先将表(collection)user 删除掉，以便演示效果

    > db.user.drop();
    true
    > show collections;
    system.indexes
    >

然后导入数据

    [root@localhost bin]# ./mongoimport -d my_mongodb -c user user.dat
    connected to: 127.0.0.1
    imported 2 objects
    [root@localhost bin]#

可以看到导入数据的时候会隐式创建表结构

###2 导入CSV数据

我们先将表user 删除掉，以便演示效果

    > db.user.drop();
    true
    > show collections;
    system.indexes
    >

然后导入数据

    [root@localhost bin]# ./mongoimport -d my_mongodb -c user --type csv --headerline --file
    user_csv.dat
    connected to: 127.0.0.1
    imported 3 objects
    [root@localhost bin]#

参数说明:

- -type 指明要导入的文件格式
- -headerline 批明不导入第一行，因为第一行是列名
- -file 指明要导入的文件路径

注意:

CSV 格式良好，主流数据库都支持导出为CSV 的格式，所以这种格式非常利于异构数据迁移

##数据备份mongodump

可以用mongodump 来做MongoDB 的库或表级别的备份，下面举例说明:

###备份my_mongodb 数据库

    [root@localhost bin]# ./mongodump -d my_mongodb
    connected to: 127.0.0.1
    DATABASE: my_mongodb to dump/my_mongodb
    my_mongodb.system.indexes to dump/my_mongodb/system.indexes.bson
    1 objects
    my_mongodb.user to dump/my_mongodb/user.bson
    2 objects
    [root@localhost bin]# ll
    总计 67648
    -rwxr-xr-x 1 root root 7508756 2011-04-06 bsondump
    drwxr-xr-x 3 root root 4096 04-10 23:54 dump
    -rwxr-xr-x 1 root root 2978016 2011-04-06 mongo

此时会在当前目录下创建一个dump 目录，用于存放备份出来的文件

也可以指定备份存放的目录，

    [root@localhost bin]# ./mongodump -d my_mongodb -o my_mongodb_dump
    connected to: 127.0.0.1
    DATABASE: my_mongodb to my_mongodb_dump/my_mongodb
    my_mongodb.system.indexes to
    my_mongodb_dump/my_mongodb/system.indexes.bson
    1 objects
    my_mongodb.user to my_mongodb_dump/my_mongodb/user.bson
    2 objects
    [root@localhost bin]#

这个例子中将备份的文件存在了当前目录下的my_mongodb_dump 目录下

##数据恢复mongorestore

由于刚刚已经做了备份，所以我们先将库my_mongodb 删除掉

    > use my_mongodb
    switched to db my_mongodb
    > db.dropDatabase()
    { "dropped" : "my_mongodb", "ok" : 1 }
    > show dbs
    admin (empty)
    local (empty)
    test (empty)
    >

接下来我们进行数据库恢复

    [root@localhost bin]# ./mongorestore -d my_mongodb my_mongodb_dump/*
    connected to: 127.0.0.1
    Wed Apr 11 00:03:03 my_mongodb_dump/my_mongodb/user.bson
    Wed Apr 11 00:03:03 going into namespace [my_mongodb.user]
    Wed Apr 11 00:03:03 2 objects found
    Wed Apr 11 00:03:03 my_mongodb_dump/my_mongodb/system.indexes.bson
    Wed Apr 11 00:03:03 going into namespace [my_mongodb.system.indexes]
    Wed Apr 11 00:03:03 { name: "_id_", ns: "my_mongodb.user", key: { _id: 1 }, v: 0 }
    Wed Apr 11 00:03:03 1 objects found
    [root@localhost bin]#

经验证数据库又回来了，其实要是想恢复库，也大可不必先删除my_mongodb 库，只要指明 –drop 参数，就可以在恢复的时候先删除表然后再向表中插入数据

