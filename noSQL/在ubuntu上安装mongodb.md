#在ubuntu上安装mongodb

计算机：32位，ubuntu操作系统。

采用安装方法参考：[http://www.cnblogs.com/alexqdh/archive/2011/11/25/2263626.html](http://www.cnblogs.com/alexqdh/archive/2011/11/25/2263626.html)

进入mongod所在的目录（/usr/bin），然后运行“./mongod --dbpath /var/lib/mongodb/ --logpath /var/log/mongodb/mongodb.log --logappend &”

    --dbpath：指定mongo的数据库文件在哪个文件夹（也就是说我本地的数据库文件存储在/var/lib/mongodb/内）

    --logpath：指定mongo的log日志是哪个，这里log一定要指定到具体的文件名

    --logappend：表示log的写入是采用附加的方式，默认的是覆盖之前的文件

    &：表示程序在后台运行

注意：如果是系统非正常关闭，这样启动会报错，由于mongodb自动被锁上了，这是需要进入mongodb数据库文件所在的目录（/var/lib/mongodb/）,删除目录中的mongodb.lock文件,然后再进行上述操作。

另外，推荐按照官方安装，这样可以得到最新版本：http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

    service mongodb start    #开始运行

    service mongodb stop

    service mongodb restart

在浏览器中：http://localhost:27017     (估计是端口被占领了，我的系统上居然得用28017端口）

