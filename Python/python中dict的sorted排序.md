#python中dict的sorted排序

我们知道Python的内置dictionary数据类型是无序的，通过key来获取对应的value。可是有时我们需要对dictionary中的item进行排序输出，可能根据key，也可能根据value来排。到底有多少种方法可以实现对dictionary的内容进行排序输出呢？下面摘取了一些精彩的解决办法。

##按key排序

###最简单的方法，这个是按照key值排序：

    def sortedDictValues1(adict):
        items = adict.items()
        items.sort()
        return [value for key, value in items]

###又一个按照key值排序，貌似比上一个速度要快点

    def sortedDictValues2(adict):
        keys = adict.keys()
        keys.sort()
        return [dict[key] for key in keys]

###还是按key值排序，据说更快。。。而且当key为tuple的时候照样适用

    def sortedDictValues3(adict):
        keys = adict.keys()
        keys.sort()
        return map(adict.get, keys)

###一行语句搞定：

    [(k,di[k]) for k in sorted(di.keys())]

##按value排序

###根据value排序的，先把item的key和value交换位置放入一个list中，再根据list每个元素的第一个值，即原来的value值，排序：

    def sort_by_value(d):
        items=d.items()
        backitems=[[v[1],v[0]] for v in items]
        backitems.sort()
        return [ backitems[i][1] for i in range(0,len(backitems))]

###还是一行搞定：

    [ v for v in sorted(d.values())]

###用lambda表达式来排序，更灵活：

    sorted(d.items(), lambda x, y: cmp(x[1], y[1]))

或反序：

    sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

##用sorted函数的key=参数

###按照key进行排序

    print sorted(dict1.items(), key=lambda d: d[0])

###按照value进行排序

    print sorted(dict1.items(), key=lambda d: d[1])

下面给出python内置sorted函数的帮助文档：

    sorted(...) 

    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

看了上面这么多种对dictionary排序的方法，其实它们的核心思想都一样，即把dictionary中的元素分离出来放到一个list中，对list排序，从而间接实现对dictionary的排序。这个“元素”可以是key，value或者item。

var   http://hi.baidu.com/jackleehit/blog/item/53da32a72207bafa9052eea1.html

