#CentOS上安装POCO

##POCO是什么？

看[官网](http://pocoproject.org/)说明：

>Modern, powerful open source C++ class libraries and frameworks for building network- and internet-based applications that run on desktop, server, mobile and embedded systems. 

##下载地址

强烈建议，唯一下载地址就是官方网站，不要图省事在某些国内站点下载。地址是：[http://pocoproject.org/download/index.html](http://pocoproject.org/download/index.html)

##安装过程

网上有很多安装实例，但是，我在CentOS7中按照那些方法实施，总是遇到问题。于是发挥自己的探索精神，终于按照下面步骤搞定，记录下来，供自己和朋友们参考

第一步：安装MySQL和ODBC

    # yum -y install unixODBC
    # yum -y install unixODBC-devel
    # yum -y install mysql
    # yum -y install mysql-devel

如果不安装，在安装POCO的时候需要声明忽略。具体看的后面步骤。

第二步：安装POCO

    # gunzip poco-X.Y.tar.gz
    # tar -xf poco-X.Y.tar
    # cd poco-X.Y
    # ./configure
    # gmake -s

以上步骤中，已经假设第一步安装了MySQL和ODBC，如果用户不安装，需要在./configure指定目录的这一步进行声明。

参数解释:  --omit 排除(不编译的), --prefix安装路径，命令样例(prefix部分可以不写)：

    # ./configure --omit=Data/ODBC,Data/SQLite --prefix=/usr  --static --shared

如果没有  --static --shared 默认为 shared 不编译静态库

附加一条来自网络的经验：

>如果在x64的系统下使用到静态库 .记得一定要加-fPIC,动态库不用.
> ./configure --omit=Data/ODBC,Data/SQLite --prefix=/usr --cflags=-fPIC --static

以上做好，最后一个命令不要忘记：

    # gmake -s install

至此，在CentOS7上安装POCO成功结束。
