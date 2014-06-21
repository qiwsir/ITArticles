#tornado安装

Tornado，中文含义是龙卷风，但是这里不是谈论这种自然现象了。当然是软件。

根据维基百科中文的介绍：

Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，由FriendFeed公司在自己的网站FriendFeed中使用，被Facebook收购以后框架以开源软件形式开放给大众。

它的性能怎么呢？

在维基百科上有人做了比较：

Tornado有着优异的性能。它试图解决C10k问题，即处理大于或等于一万的并发，下表是和一些其他Web框架与服务器的对比:
处理器为 AMD Opteron, 主频2.4GHz, 4核服务	

|         |部署           |请求/每秒|
|---------|:-------------:|--------:|
Tornado   |nginx,4进程    |8213     |
|Tornado  |1个单线程进程   |3353     |
|Django   |Apache/mod_wsgi|2223     |
|web.py   |Apache/mod_wsgi|2066     |
|CherryPy |独立           |785      |

这就足够促使我喜欢这个框架了，更何况，据说它跟所钟爱的web.py还有很多近似。

于是就开始安装：

登录官方网站：http://www.tornadoweb.org/

下载安装包，目前是tornado-3.2，到官方网站下载。

然后就安装，命令如下：

    tar xvzf tornado-3.1.tar.gz
    cd tornado-3.1
    python setup.py build
    sudo python setup.py install

