#md5和sha1加密

python提供了一个进行hash加密的模块：hashlib

hashlib的官方介绍地址：http://docs.python.org/2/library/hashlib.html，当然是洋文的，下面理解来自于官网和自己的使用经验。

在应用中，常用的是md5加密和sha1加密（注意，是数字1,不是字母l，这类命名，应该最大限度避免。）

##md5

md5的全称是Message-Digest Algorithm 5（信息-摘要算法）。128位长度。目前md5是一种不可逆算法。 具有很高的安全性。它对应任何字符串都可以加密成一段唯一的固定长度的代码。  

##sha1

sha1的全称是Secure Hash Algorithm(安全哈希算法) 。SHA1基于MD5，加密后的数据长度更长， 它对长度小于264的输入，产生长度为160bit的散列值。比md5多32位。 因此，比MD5更加安全，但SHA1的运算速度就比MD5要慢了。  

##Python中的用法 

Python 内置的 hashlib 模块就包括了 md5 和 sha1 算法。使用方法：

###以MD5为例：

    import hashlib

    data =  'This a md5 test!'

    hash_md5 = hashlib.md5(data)

    hash_md5.hexdigest()

输出：

    '0a2c0b988863f08471067903d8737962'

上面这段字符串就是 data 转换后的MD5值。  

MD5的用途：    

- 加密网站注册用户的密码。    
- 网站用户上传图片 / 文件后，计算出MD5值作为文件名。（MD5可以保证唯一性）    
- key-value数据库中使用MD5值作为key。    
- 比较两个文件是否相同。（大家在下载一些资源的时候，就会发现网站提供了MD5值，就是用来检测文件是否被篡改）    
    ……  

###sha1的使用

与MD5类似：

    import hashlib
    hashlib.sha1('This is a sha1 test!').hexdigest()      

###处理大文件

上面说过可以用MD5来检测两个文件是否相同，但想想，如果是两个很大的文件，担心内存不够用，这时怎么办？ 这就要使用 update 方法了。

代码如下：

    import hashlib
    def get_file_md5(f):    
        m = hashlib.md5()    
        while True:        
            data = f.read(10240)        
            if not data:            
                break        
            m.update(data)    
        return m.hexdigest()

    with open(YOUR_FILE, 'r') as f:    
        file_md5 = get_file_md5(f)

 (windows 用户 要使用 'rb'方式打开文件)  

可以用下面这段代码验证一下：

    import hashlib

    x = hashlib.md5()
    x.update('hello, ')
    x.update('python')
    x.hexdigest()

    hashlib.md5('hello, python').hexdigest()

这两次的输出是一样的。 SHA1 也是一样的用法。

参考：http://www.cnblogs.com/the4king/archive/2012/02/06/2340660.html

