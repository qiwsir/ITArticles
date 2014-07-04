#python之UTF-8解决方案

答案1：使用Python3

直到目前，还更多使用python2.7的。看下面答案：

    # -*- coding: utf8 -*-
    # 及早将一切转到UTF-8
    unicode_str = unicode('中文', encoding='utf-8')
    # 打印或者写入前用UTF-8编码
    print unicode_str.encode('utf-8')
    # 用codecs.open替换open
    import codecs
    codecs.open('filename', encoding='utf8')

