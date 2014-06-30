#python连接mysql

尽量不用框架内的数据库连接方式。特别是在tornado中，我提倡用python通过MySQLdb连接mysql数据库。虽然在tornado2.4有tornado.database，在tornado3.0有torndb。但是，为了性能，还是不推荐用这些。

做为程序员，必须写SQL语句，除非不用。

##下载安装MySQLdb

MySQLdb模块是python连接mysql数据库的一个模块，在操作mysql数据库是经常使用。

windows下略，只提供linux方式。

**方法一：**

下载地址：http://sourceforge.net/projects/mysql-python/

先安装setuptools，

然后在下载文件目录下，修改mysite.cfg,指定本地mysql的mysql-config文件的路径

这里有更多的内容，包括源码和安装文档：https://github.com/farcepest/MySQLdb1

**方法二：针对ubuntu操作系统**

前提：已经在Ubuntu下安装了easy_install，若没有，可以执行命令：

    sudo apt-get install python-setuptools python-dev build-essential

安装完成以后，就可以利用easyinstall 安装需要的模块。

安装MySQLdb:

    sudo easy_install mysql-python

有可能报错，曾遇到一种错误提示：

    "the required version of distribute(>=0.6.28) is not available"

这是要安装 libmysqld-dev，安装方法：

    sudo apt-get install libmysqld-dev

再安装mysql-python,OK。

##数据库的连接

用下面的方法连接数据库：

    import MySQLdb

    conn=MySQLdb.connect(host="localhost",user="root",passwd="111111",db="yeashape",charset="utf8")

    #yeahape是数据库名称

connect函数的参数详解：（一般情况下用默认值，不用修改，即可省略）

- host，连接的数据库服务器主机名，默认为本地主机(localhost)。
- user，连接数据库的用户名，默认为当前用户。
- passwd，连接密码，没有默认值。
- db，连接的数据库名，没有默认值。
- conv，将文字映射到Python类型的字典。默认为MySQLdb.converters.conversions
- cursorclass，cursor()使用的种类，默认值为MySQLdb.cursors.Cursor。
- compress，启用协议压缩功能。
- named_pipe，在windows中，与一个命名管道相连接。
- init_command，一旦连接建立，就为数据库服务器指定一条语句来运行。
- read_default_file，使用指定的MySQL配置文件。
- read_default_group，读取的默认组。
- unix_socket，在unix中，连接使用的套接字，默认使用TCP。
- port，指定数据库服务器的连接端口，默认是3306

##其它连接对象的方法

- 连接对象的db.close()方法可关闭数据库连接，并释放相关资源。
- 连接对象的db.cursor([cursorClass])方法返回一个指针对象，用于访问和操作数据库中的数据。
- 连接对象的db.begin()方法用于开始一个事务，如果数据库的AUTOCOMMIT已经开启就关闭它，直到事务调用commit()和rollback()结束。
- 连接对象的db.commit()和db.rollback()方法分别表示事务提交和回退。
- 指针对象的cursor.close()方法关闭指针并释放相关资源。
- 指针对象的cursor.execute(query[,parameters])方法执行数据库查询。
- 指针对象的cursor.fetchall()可取出指针结果集中的所有行，返回的结果集一个元组(tuples)。
- 指针对象的cursor.fetchmany([size=cursor.arraysize])从查询结果集中取出多行，我们可利用可选的参数指定取出的行数。
- 指针对象的cursor.fetchone()从查询结果集中返回下一行。
- 指针对象的cursor.arraysize属性指定由cursor.fetchmany()方法返回行的数目，影响fetchall()的性能，默认值为1。
- 指针对象的cursor.rowcount属性指出上次查询或更新所发生行数。-1表示还没开始查询或没有查询到数据。

