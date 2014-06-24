#Python--字典

##定义

字典由大括号内的多个键值对组成，如：phonebook={'Alice':'2341','Beth':'9102','Cecil':'3258'}

##字典的创建

###1.直接创建：

phonebook={'Alice':'2341','Beth':'9102','Cecil':'3258'} （键和值用冒号隔开，各个键值对键用逗号隔开）    

###2.dict函数：        

    >>>items=[('name','Gumby'),('age',42)] #dict的第一种方法        
    >>>d=dict(items)            
        {'age':42,'name':'Gumby'}        
    >>>d=dict(name='Gumby',age=42) #dict的第二种方法            
        {'age':42,'name':'Gumby'}        
    >>>d['***al']='boy'             
        {'age':42,'name':'Gumby','***ual':'boy'}

##字典的格式化字符串

在转换说明符中的%字符后面，可以加上用圆括号括起来的键，后面再更其他说明元素。        

    phonebook={'Alice':'2341','Beth':'9102','Cecil':'3258'}         

    print "Alice's phone number is  %(Alice)s,Cecil's phone number is %(Cecil)s" % phonebook    #%(Alice)s的s表示输出字符串的意思

    -->Alice's phone number is 2341,Cecil's phone number is 3258    

注：这类字符串格式化在模板系统中非常有用，string.Template类对于这类应用也是非常有用的。

##字典的方法

- clear

清除字典中的所有项：

    phonebook.clear() #phonebook是一个字典对象

- copy

浅复制：只复制字典中的父对象，对子对象采取引用的办法。改变子对象的内容会影响到复制和被复制的字典。

例：

    x={'username':'admin','machines':['foo','bar','baz']}
    y=x.copy()
    y['username']='Allen'
    y['machines'].remove('bar')
    print y
    print x

输出：

    {'username':'Allen','machines':['foo','baz']} #y
    {'username':'admin','machines':['foo','baz']} #x 链表子对象中的值改变，会影响两个字典。子对象采取应用的方法。

- deepcopy

深度复制：完全复制，新字典的改变不会影响原来的字典。

    from copy import deepcopy
    d={'username':'admin','machines':['foo','bar','baz']}
    dc=deepcopy(d)

- fromkeys
 
使用给定的键建立新的字典，每个键默认对应的值为None。

    {}.fromkey(['name','age'])
    -->{'age':None,'name':None}
    dict.fromkey(['name','age']) #直接在所有字典的类型dict上调用方法
    -->{'age':None,'name':None}
    dict.fromkey(['name','age']，'(unknown)') #不用None作为默认值，自己提供默认值
    -->{'age':'(unknown)','name':'(unknown)' }

- get

get方法是一个更宽松的访问字典项的方法。一般来说，如果试图访问字典中不存在的项时会出错。而用get就不会。

例：

    >>>d={} #空字典
    >>>print d['name']
    Traceback........ #出错信息
    >>>print d.get('name')
    None  #可以自定义默认值代替None，如d.get('name','N/A'),如果没有name项就打印N/A

- has_key

检查字典中是否含有给出的键。d.has_key(k)相当于k in d。Python3.0中不包含这个函数。

    >>>d={'name':'fuss'}
    >>>d.has_key('age')
    False
    >>>d.has_key('name')
    True

- items和iteritems

items方法将所有字典项以列表方式返回。

    >>> d={'name':'fu','age':24,'***al':'boy'}
    >>> d.items()
       [('age', 24), ('name', 'fu'), ('***ual', 'boy')] #返回没有特殊的顺序

iteritems方法的作用大致相同，但是会返回一个迭代器对象而不是列表：

    >>> it=d.iteritems()
    >>> it
        <dictionary-itemiterator object at 0x011DA580>
    >>> list(it)
        [('age', 24), ('name', 'fu'), ('***ual', 'boy')]

- keys和iterkeys
  
keys方法将字典中的键以列表的形式返回，而iterkeys则返回针对键的迭代器。

    >>>d.keys()
    ['age', 'name', '***ual']

- pop

用来获得对应于给定键的值，然后将这个键值对从字典移除。

    >>>d={'x':1,'y':2}
    >>>d.pop('x')
        1
    >>>d
       {'y':2}

- popitem
  
popitem方法类似于list.pop，后者会弹出列表的最后一个元素。但popitem弹出的是随机项，以为字典没有"最后的元素"或其他有关顺序的概念。

    >>>d={'x':1,'y':2} 
    >>>d.popitem()
        ('x':1) #随机的

- setdefault
  
setdefault方法在某种程度上类似于get方法，就是能获得与给定键关联的值，除此之外，setdefault还能在字典中不含有给定键的情况下设定相应的键值。

    >>>d={}
    >>>d.setdefault('name','N/A')
      'N/A'
    >>>d
      {'name':'N/A'}
    >>>d['name']='Allen'
    >>>d.setdefault('name','N/A')
        'Allen'
    >>>d
        {'name':'Allen'}

- update
  
update方法可以利用一个字典项更新另外一个字典：

    >>>d={'x':123,'y':456}
    >>>b={'x':789}
    >>>d.update(b)
    >>>d
    {'x':789,'y':456}

提供的字典项会被添加到旧的字典中，若有相同的键则会进行覆盖。

- values和itervalues
  
values方法一列表的形式返回字典的值(itervalues返回值的迭代器)。与keys对比(对应关系)

例：

    d={'name':'fu','age':24,'***ual':'boy'}
    print d.keys()       #返回字典的键列表    
    print d.values()    #返回字典的值列表
    ['age', 'name', '***ual']  #键列表 
    ['fu',24,'boy']   #值列表


