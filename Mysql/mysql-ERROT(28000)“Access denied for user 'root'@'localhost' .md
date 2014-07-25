#mysql登录报错“Access denied for user 'root'@'localhost' (using password: YES”的处理方法

这个问题常常出现在连接某些远程服务器，运行其mysql数据库的时候。

最近登录某台服务器的mysql时候总报错：

    Access[root@log01 ~]# mysql -u root -p
    Enter password: 
    ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO) denied for user 'root'@'localhost' (using password: NO)

我猜想是不是密码忘记了。。。然后准备修改密码：

    #mysqladmin -u root -p password 123456     ###设置root密码为123456
    Enter password: 
    mysqladmin: connect to server at 'localhost' failed
    error: 'Access denied for user 'root'@'localhost' (using password: YES)'

依然报这个错误。。。蛋疼了，百度一下，最终找到了方法如下：

##方法一：（此方法我已经使用过，通过） 

    # /etc/init.d/mysqld stop 
    # mysqld_safe --user=mysql --skip-grant-tables --skip-networking & 
    # mysql -u root mysql 
    mysql> UPDATE user SET Password=PASSWORD(’newpassword’) where USER=’root’; 
    mysql> FLUSH PRIVILEGES; 
    mysql> quit 
    # /etc/init.d/mysqld restart 
    # mysql -uroot -p 
    Enter password: <输入新设的密码newpassword> 
    mysql> 

##方法二： 

直接使用/etc/mysql/debian.cnf文件中[client]节提供的用户名和密码: 

    # mysql -udebian-sys-maint -p 
    Enter password: <输入[client]节的密码> 
    mysql> UPDATE user SET Password=PASSWORD(’newpassword’) where USER=’root’; 
    mysql> FLUSH PRIVILEGES; 
    mysql> quit 
    # mysql -uroot -p 
    Enter password: <输入新设的密码newpassword> 
    mysql> 

##方法三： 

这种方法我没有进行过测试，因为我的root用户默认密码已经被我修改过了，那位有空测试一下，把结果告诉我，谢谢！ 

    # mysql -uroot -p 
    Enter password: <输入/etc/mysql/debian.cnf文件中[client]节提供的密码> 

至此，困惑多时的问题解决了！
 

本文出自 “苦咖啡's运维之路” 博客，请务必保留此出处http://alsww.blog.51cto.com/2001924/1121676

