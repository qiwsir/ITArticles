#解决类似`/usr/lib64/libstdc++.so.6: version 'GLIBCXX_3.4.19' not found`错误

运行MonaServer的时候，遇到了下面的报错：

    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.19' not found (required by ./MonaServer)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./MonaServer)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.15' not found (required by ./../MonaBase/lib/libMonaBase.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./../MonaBase/lib/libMonaBase.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.19' not found (required by ./../MonaBase/lib/libMonaBase.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.17' not found (required by ./../MonaCore/lib/libMonaCore.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.19' not found (required by ./../MonaCore/lib/libMonaCore.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./../MonaCore/lib/libMonaCore.so)
    ./MonaServer: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.15' not found (required by ./../MonaCore/lib/libMonaCore.so)
    
执行：
    # strings /usr/lib64/libstdc++.so.6|grep GLIBCXX

得到结果：
  
    GLIBCXX_3.4
    GLIBCXX_3.4.1
    GLIBCXX_3.4.2
    GLIBCXX_3.4.3
    GLIBCXX_3.4.4
    GLIBCXX_3.4.5
    GLIBCXX_3.4.6  
    GLIBCXX_3.4.7
    GLIBCXX_3.4.8
    GLIBCXX_3.4.9
    GLIBCXX_3.4.10
    GLIBCXX_3.4.11
    GLIBCXX_3.4.12
    GLIBCXX_3.4.13
    GLIBCXX_FORCE_NEW
    GLIBCXX_DEBUG_MESSAGE_LENGTH
    
到13到头了，所以报错啦。

##解决方法

###到编译时的目录下面找到文件：libstdc++.so.6.0.18

我编译的时候，建立build_gcc_4.8.1文件夹，具体方法参见：[centos升级gcc到4.8.1](https://github.com/qiwsir/ITArticles/blob/master/Linux/upgrade_gcc_on_Centos.md)

注意，进入目录是，.libs是隐藏的：/home/build_gcc_4.8.1/x86_64-unknown-linux-gnu/libstdc++-v3/src/.libs

![](http://wxpictures.qiniudn.com/glibcxxerror.png)

用下面的命令查看：

    strings libstdc++.so.6.0.18|grep GLIBCXX
    
一般来讲，里面就有满足需要的GLIBCXX版本了。

然后，把该文件拷贝到了/usr/lib64下.

然后将libstdc++.so.6指向libstdc++.so.6.0.18:

    [root@localhost lib64]# rm -r libstdc++.so.6
    rm: remove symbolic link `libstdc++.so.6'? y
    [root@localhost lib64]# ln -s libstdc++.so.6.0.18 libstdc++.so.6

这就Ok了。
