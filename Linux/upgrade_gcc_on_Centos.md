#centos升级gcc到4.8.1(支持c++11)步骤

##下载gcc最新版

    wget http://ftp.gnu.org/gnu/gcc/gcc-4.8.1/gcc-4.8.1.tar.gz

然后解压到文件夹

    tar -xvzf gcc-4.8.1.tar.gz

进入解压缩之后的目录

    cd gcc-4.8.1

然后执行下面的运行

    ./contrib/download_prerequisites

再返回上一层，建立`build_gcc_4.8.1`目录，这个目录和gcc-4.8.1平行

    cd ..
    mkdir build_gcc_4.8.1

进入刚建立的目录，并执行编译过程

    cd build_gcc_4.8.1
    ../gcc-4.8.1/configure --enable-checking=release --enable-languages=c,c++ --disable-multilib  
    make -j23
    make install

OK,在build_gcc_4.8.1中将gcc已经安装完成

确定新安装的GCC的路径，之前安装时记下最后mv时的路径即可，我是默认安在了/usr/local/bin

    ls /usr/local/bin | grep gcc

看图

![](http://wxpictures.qiniudn.com/binx86.png)

执行

    /usr/sbin/update-alternatives --install  /usr/bin/gcc gcc /usr/local/bin/x86_64-unknown-linux-gnu-gcc-4.8.1 40

    gcc --version      #查看版本

    /usr/sbin/update-alternatives --install /usr/bin/g++ g++ /usr/local/bin/g++ 40

    g++ --version     #查看版本



来源：http://lonelyprogram.blog.51cto.com/6246243/1355261
