#dict字典遍历方法

##python dict遍历：

1、 for in

2、 items

3、 iteritems

##举例：

    >>> dict={"name":"python","english":33,"math":35}
    >>> dict         
    {'name': 'python', 'math': 35, 'english': 33}
    >>> for i in dict:
    ...     print "dict[%s]"%i,dict[i]
    ...

    dict[name] python
    dict[math] 35
    dict[english] 33
    
    >>> for i in dict:
    ...     print dict[i]
    ...
    python
    35
    33

    >>> for (k,v) in dict.items():
    ...     print "dict[%s]="%k,v
    ...
    dict[name]= python
    dict[math]= 35
    dict[english]= 33


    >>> for (k,v) in dict.items():
    ...     print k,v
    ...
    name python
    math 35
    english 33


    >>> for k,v in dict.iteritems():
    ...     print "dict[%s]="%k,v
    ...
    dict[name]= python
    dict[math]= 35
    dict[english]= 33

