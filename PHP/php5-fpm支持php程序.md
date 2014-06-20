#php5-fpm支持php程序

阿里云的云服务器,配置是512M内存.

原来已经通过cgi跑着一个python项目.后来又通过spawn-fcgi跑php项目.

结果是,cpu使用率达到了100%,系统直接挂了.

解决方案是:采用php5-fpm

##什么是php-fpm

PHP-FPM是一个PHPFastCGI管理器，是只用于PHP的。

相对Spawn-FCGI，PHP-FPM在CPU和内存方面的控制都更胜一筹，而且前者很容易崩溃，必须用crontab进行监控，而PHP-FPM则没有这种烦恼。

PHP5.3.3已经集成php-fpm了，不再是第三方的包了。

PHP-FPM提供了更好的PHP进程管理方式，可以有效控制内存和进程、可以平滑重载PHP配置，比spawn-fcgi具有更多优点，所以被PHP官方收录了。

##操作

首先停止fastcgi进程

去掉spawn-fcgi开机启动：

/usr/sbin/update-rc.d -f php-fastcgi remove

接着就可以开启（关闭、重启）php-fpm：

开启:/etc/init.d/php5-fpm start

关闭:/etc/init.d/php5-fpm  stop

重启:/etc/init.d/php5-fpm restart

如果想php-fpm开机启动，可以执行者命令：

/usr/sbin/update-rc.d php5-fpm defaults

##配置和说明

关于 php-fpm配置（配置默认放在/etc/php5/fpm/php-fpm.conf）的说明,网上很多,随意搜索即可.

特别说明的是,在php5的php-fpm.conf配置中,此文件夹中有pool.d子目录,php-fpm.conf是公共配置,如果对某一个服务有单独配置,可以到pool.d中进行.

此外,如果遇到在开启或者重启不成功的话,最可能的是此处的配置有错误.

