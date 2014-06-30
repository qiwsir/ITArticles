#Python Collection 小技巧

独立软件开发者 Alex Marandon 在他的博客中介绍了数个关于 Python Collection 的实用小技巧，在此与诸位分享。

##判断一个 list 是否为空

传统的方式：

    if len(mylist):
        # Do something with my list
    else:
        # The list is empty

由于一个空 list 本身等同于 False，所以可以直接：

    if mylist:
        # Do something with my list
    else:
        # The list is empty

##遍历 list 的同时获取索引

传统的方式：

    i = 0
    for element in mylist:
        # Do something with i and element
        i += 1

这样更简洁些：

    for i, element in enumerate(mylist):
        # Do something with i and element
        pass

##list 排序

在包含某元素的列表中依据某个属性排序是一个很常见的操作。例如这里我们先创建一个包含 person 的 list：

    class Person(object):
        def __init__(self, age):
            self.age = age

    persons = [Person(age) for age in (14, 78, 42)]

传统的方式是：

    def get_sort_key(element):
        return element.age

    for element in sorted(persons, key=get_sort_key):
        print "Age:", element.age

更加简洁、可读性更好的方法是使用 Python 标准库中的 operator 模块：

    from operator import attrgetter

    for element in sorted(persons, key=attrgetter('age')):
        print "Age:", element.age

attrgetter 方法优先返回读取的属性值作为参数传递给 sorted 方法。operator 模块还包括 itemgetter 和 methodcaller 方法，作用如其字面含义。

##在 Dictionary 中元素分组

和上面类似，先创建 Persons：

    class Person(object):
    def __init__(self, age):
            self.age = age

    persons = [Person(age) for age in (78, 14, 78, 42, 14)]

如果现在我们要按照年龄分组的话，一种方法是使用 in 操作符：

    persons_by_age = {}

    for person in persons:
        age = person.age
        if age in persons_by_age:
            persons_by_age[age].append(person)
        else:
            persons_by_age[age] = [person]

    assert len(persons_by_age[78]) == 2

相比较之下，使用 collections 模块中 defaultdict 方法的途径可读性更好：

    from collections import defaultdict

    persons_by_age = defaultdict(list)

    for person in persons:
        persons_by_age[person.age].append(person)

defaultdict 将会利用接受的参数为每个不存在的 key 创建对应的值，这里我们传递的是 list，所以它将为每个 key 创建一个 list 类型的值。

内容来源：AlexMarandon.com

