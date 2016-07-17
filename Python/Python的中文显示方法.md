#Python2.x的中文显示方法

python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，python的处理常常会报这样的错

    UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position 1: ordinal not in range(128)，

python没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。

查询系统默认编码可以在解释器中输入以下命令： Python代码    

    >>>sys.getdefaultencoding() 

设置默认编码时使用： Python代码    

    >>>sys.setdefaultencoding('utf8')  

可能会报

    AttributeError: 'module' object has no attribute 'setdefaultencoding'    

的错误，执行reload(sys)，在执行以上命令就可以顺利通过。

此时在执行sys.getdefaultencoding()就会发现编码已经被设置为utf8的了，但是在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了，那么有没有办法一次性修改程序或系统的默认编码呢。  

###有2种方法设置python的默认编码：

一个解决的方案在程序中加入以下代码： Python代码    

    import sys 
    reload(sys) 
    sys.setdefaultencoding('utf8')   

另一个方案是在/usr/local/lib/python.27/site-packages或者/usr/lib/python2.7下新建一个sitecustomize.py，内容为： Python代码，
两个路径的原因是因为系统不同的原因，debian和ubuntu存放的目录是后者，其他没有测试。 

    # encoding=utf8 

    import sys   
    reload(sys) 
    sys.setdefaultencoding('utf8')  

重启python解释器，执行sys.getdefaultencoding()，发现编码已经被设置为utf8的了，多次重启之后，效果相同，这是因为系统在python启动的时候，自行调用该文件，设置系统的默认编码，而不需要每次都手动的加上解决代码，属于一劳永逸的解决方法。  

还有一种解决方案是在程序中所有涉及到编码的地方，强制编码为utf8，即添加代码encode("utf8")，这种方法并不推荐使用，因为一旦少写一个地方，将会导致大量的错误报告.

来源：http://blog.sina.com.cn/s/blog_6b1ed4fb01019d4n.html
来源：http://blog.sina.com.cn/s/blog_494e45fe0102e3p9.html
