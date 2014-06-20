#网站性能压力测试工具WebBench

Webbench是由[Lionbridge公司](http://www.lionbridge.com)开发，是知名的网站压力测试工具。

##在debian 上的安装方法：

在 http://home.tiscali.cz/~cz210552/webbench.html 找到最新版

    wget http://home.tiscali.cz/~cz210552/distfiles/webbench-1.5.tar.gz

    tar zxvf webbench-1.5.tar.gz

    cd webbench-1.5

    make

    make install

如果make 时提示出错：

    ctags: not found

则安装它

    apt-get install ctags

测试格式：

    webbench -c 1000 -t 60 http://localhost/

    webbench -c 并发数 -t 运行测试时间 URL

