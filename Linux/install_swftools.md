#在ubuntu上安装swftools

##关于swftools

官方网站：www.swftools.org

解释：

>SWFTools is a collection of utilities for working with Adobe Flash files (SWF files). The tool collection includes programs for reading SWF files, combining them, and creating them from other content (like images, sound files, videos or sourcecode). SWFTools is released under the GPL. 

##swftools安装过程

###依赖组件

1. 安装freetype

下载地址：http://www.freetype.org/

安装流程：

    tar -xjf freetype-2.5.5.tar.bz2         #以下载的是freetype-2.5.5.tar.bz2为例
    cd freetype-2.5.5
    ./configure
    make
    sudo make install

2. 安装JPEG Group

下载地址：http://www.ijg.org/

安装流程：

    tar -xvzf jpegsrc.v9a.tar.gz
    cd jpeg-9a
    ./configure
    make
    sudo make install

###安装swftools

从官方网站下载之后，解压缩(我在这里用的是github上的版本，直接：git clone https://github.com/brad/swftools.git)

    cd swftools
    ./configure
    make
    sudo make install

上面的方法，是在比较顺利的时候，就那么顺利地完成了。或许，有下面的问题。

安装完成后执行一下，pdf2swf -h 有帮助内容显示，则证明安装成功。

如果所转换的PDF不包含中文，则到此为止就可以正常使用了。

如果包含中文，就需要使用到xpdf的字体库。

###问题和解法

出现报错信息：

     :info:build jpeg.c:109:35: error: use of undeclared identifier 'TRUE'
     :info:build   jpeg_set_quality(&cinfo,quality,TRUE);
     :info:build

解决方法：

到swftools的源码中，修改文件：lib/jpeg.c:

原来为：

    #ifdef HAVE_JPEGLIB
    #define HAVE_BOOLEAN
    #include

将上述部分修改为：   

    #ifdef HAVE_JPEGLIB
    #ifndef FALSE           
    #define FALSE   0       
    #endif
    #ifndef TRUE
    #define TRUE    1
    #endif
    #define HAVE_BOOLEAN
    #include

##更多参考资料

- https://trac.macports.org/ticket/42735
- http://iwang.github.io/miranda/2013/12/15/install-swftools-ubuntu.html
- http://shitouququ.blog.51cto.com/24569/1252930
- http://blog.sina.com.cn/s/blog_6094008a0102vney.html
