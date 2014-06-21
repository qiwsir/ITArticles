#python和web.py的HTML字符转义

##Python处理HTML转义字符

抓网页数据经常遇到例如&gt;或者&nbsp;这种HTML转义符，抓到字符串里很是烦人。

比方说一个从网页中抓到的字符串

    s = '&lt;abc&gt;' 

用Python可以这样处理：

    import　 HTMLParser

    html_parser = HTMLParser.HTMLParser()

    s = html_parser.unescape(s)  #这样就得到了s = '<abc>'

##url 上的转义

    import urllib

    urllib.quote

###反函数 unquote

用这个函数，会遇到一个问题，就是编辑器中输入的内容如果含有空格，会自动转义成“＋”.

解决方法是用:urllib.quote_plus()

##html 中保留字符(eg: ><)转义
    
    import cgi

    cgi.escape 

##webpy模板自动HTML转义

要注意 web.py 将会转义任何任何用到的变量，所以当你将 name 的值设为是一段 HTML 时，它会被转义显示成纯文本。

如果要关闭该选项，可以写成 $:name 来代替 $name。

如果我们想部分转移，怎么办？ webpy显然提供了转移函数，我们在应用层直接调用就可以了。

    from  web.net  import  htmlquote

    htmlquote(raw_text)

