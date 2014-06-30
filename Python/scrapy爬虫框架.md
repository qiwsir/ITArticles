#scrapy爬虫框架

##简介

Scrapy是用Python开发的一个快速,高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。    

Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持！    

Scrapy 使用 Twisted 这个异步网络库来处理网络通讯，架构清晰，并且包含了各种中间件接口，可以灵活的完成各种需求

##安装

在scrapy的官方网站有安装指南，见：http://doc.scrapy.org/en/latest/intro/install.html

但是，我在安装的时候，运行

    $sudo easy_install scrapy

总是出现Twisted无法安装，所以，只能到twisted网站下载，并安装。安装方法如下：

1、下载Twisted，这里 下载Twisted：https://twistedmatrix.com/trac/，注意根据自己的操作系统。我是用linux，所以直接下载source版本就可以了。找最新的啦。

2、安装Twisted 下载好Twisted后，进入到下载目录，解压：

    [root@codebreaker ~]#tar -jvxf Twisted-13.2.0.tar.bz2

解压完成后进入相应目录：

    [root@codebreaker ~]#cd Twisted-13.2.0

执行安装：

    [root@codebreaker Twisted-13.2.0]#python setup.py install

安装完成后进入python，测试Twisted是否安装成功

    [root@codebreaker Twisted-13.2.0]# python

    >>> import twisted

    >>>

如果没有错误发生，说明Twisted已经安装成功了

##创建项目

在适当的目录中，运行：

    scrapy startproject project_name       #project_name是自己的项目名称

得到如下目录结构：

    your project_name/

        scrapy.cfg    #本项目的基本设置

        your project_name/

            __init__.py

            items.py    #规定item['aaa']=Field()

            pipelines.py    #让scrapy做的事情，一般都在这里

            settings.py    #有关的设置，起到承上启下的作用

            spiders/    #将爬虫的法则写到这里

                __init__.py

具体的例子，可以到官方文档或者github上搜索。

##抓图的准备工作

scrapy抓图，是一个比较麻烦的事情。网上很多例子或者方案，不一定适合具体情况。这里罗列我在自己的环境中做的过程

环境：ubuntu12.04+python2.7

安装如下各项：

###第一步：安装zlib png freetype   jpeg

    install zlib (ubuntu 官方源没有zlib，别想apt-get了)

下载zlib，(zlib.net可能需要梯子，可以去SF.net)，（http://sourceforge.net/projects/libpng/files/zlib/1.2.5/zlib-1.2.5.tar.gz/download?use_mirror=superb-dca2）

    $ tar -xvzf zlib-1.2.5.tar.gz
    $ cd zlib-1.2.5
    $ ./configure --prefix=/usr/local
    $ make
    $ sudo make install

**install png**

到ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng16/找最新版本的下载，我发布此文的时候，是libpng-1.6.9.tar.gz，下载之后，进行如下操作：   

    $ tar -xvzf libpng-1.6.9.tar.gz
    $ cd libpng-1.6.9.tar.gz
    $ ./configure --prefix=/usr/local
    $ make
    $ sudo make install

**install freetype**

到http://nchc.dl.sourceforge.net/project/freetype/freetype2/下载最新版本，我下载是2.4.11

    $ tar -xvzf freetype-2.4.11.tar.gz
    $ cd freetype-2.4.11/
    $ ./configure --prefix=/usr/local
    $ make
    $ make install 

**install jpeg**

到http://www.ijg.org/files/下载最新版本，我下载的是jpegsrc.v9a.tar.gz

    $ tar -xvzf jpegsrc.v9a.tar.gz
    $ cd jpeg-9a/
    $ ./configure --prefix=/usr/local
    $ make
    $ sudo make install
 

###第二步：安装需要的 devel库

    $ sudo apt-get install libjpeg8-dev
    $ sudo apt-get install libpng12-dev
    $ sudo apt-get install libfreetype6-dev
    $ sudo apt-get install zlib1g-dev

###第三步：安装 Pillow

Scrpy文档中的这句话非常重要，要认真阅读一下：（http://doc.scrapy.org/en/latest/topics/images.html）

>>Pillow is used for thumbnailing and normalizing images to JPEG/RGB format, so you need to install this library in order to use the images pipeline. Python Imaging Library (PIL) should also work in most cases, but it is known to cause troubles in some setups, so we recommend to use Pillow instead of PIL.

还有这句话：

>>Convert all downloaded images to a common format (JPG) and mode (RGB)
>>Avoid re-downloading images which were downloaded recently
>>Thumbnail generation
>>Check images width/height to make sure they meet a minimum constraint

以上内容的了解，有助于对图的获取。

接下来就到 https://github.com/python-imaging/Pillow下载后将其解压缩在任一文件夹中，进入目录

    $ python setup.py build_ext -i
    running build_ext
    --------------------------------------------------------------------
    PIL SETUP SUMMARY
    --------------------------------------------------------------------
    version      Pillow 2.2.1
    platform     linux 3.3.2+ (default, Oct  9 2013, 14:50:09)
             [GCC 4.8.1]
    --------------------------------------------------------------------
    --- TKINTER support available
    --- JPEG support available      #这个必须可用，如果不可用，说明安装有误
    --- ZLIB (PNG/ZIP) support available    #要求同上
    --- TIFF G3/G4 (experimental) support available
    --- FREETYPE2 support available
    --- LITTLECMS2 support available
    --- WEBP support available
    *** WEBPMUX support not available
    --------------------------------------------------------------------
    To add a missing option, make sure you have the required
    library, and set the corresponding ROOT variable in the
    setup.py script.
    To check the build, run the selftest.py script.

然后安装：
    
    $ sudo python setup.py install

JPEG编码/解码编辑本段回目录

我在调试的时候，出现了一个问题：

    encoder jpeg not available    错误提示

网上多是讲decoder jpeg问题（解码），不是encoder编码。而且给出方案就是pil出问题，就要安装这个。并且有不少文章建议用 from PIL import Image。

我在python中做了如下检验：

    >>> import Image
    >>> Image.init()
    1
    >>> Image.SAVE.keys()
    ['PCX', 'SPIDER', 'HDF5', 'TIFF', 'BUFR', 'BMP', 'JPEG', 'EPS', 'XBM', 'GIF', 'GRIB', 'TGA', 'IM', 'PPM', 'PDF', 'FITS', 'PALM', 'MSP', 'WMF', 'PNG']

这说明用 import Image是可以的。

于是我大胆地修改了 scrapy中的pipeline/image.py文件中的from PIL import Image，将其改成 import Image。

再抓，成功！(这个问题苦恼了我2天，终于成功了。)

注：文件在：/usr/local/lib/python2.7/site-packages/Scrapy-0.22.0-py2.7.egg/scrapy/contrib/pipeline/image.py

常见错误编辑本段回目录

    ImportError: No module named pkg_resources

在root权限下运行：

    curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python

