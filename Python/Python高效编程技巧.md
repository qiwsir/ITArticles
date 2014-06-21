#Python高效编程技巧

我已经使用Python编程有多年了，即使今天我仍然惊奇于这种语言所能让代码表现出的整洁和对DRY编程原则的适用。这些年来的经历让我学到了很多的小技巧和知识，大多数是通过阅读很流行的开源软件，如Django, Flask,Requests中获得的。

下面我挑选出的这几个技巧常常会被人们忽略，但它们在日常编程中能真正的给我们带来不少帮助。

##1. 字典推导(Dictionary comprehensions)和集合推导(Set comprehensions)

大多数的Python程序员都知道且使用过列表推导(list comprehensions)。如果你对list comprehensions概念不是很熟悉——一个list comprehension就是一个更简短、简洁的创建一个list的方法。

    >>> some_list = [1, 2, 3, 4, 5]

    >>> another_list = [ x + 1 for x in some_list ]

    >>> another_list

    [2, 3, 4, 5, 6]

自从python 3.1 (甚至是Python 2.7)起，我们可以用同样的语法来创建集合和字典表：

    >>> # Set Comprehensions

    >>> some_list = [1, 2, 3, 4, 5, 2, 5, 1, 4, 8]

    >>> even_set = { x for x in some_list if x % 2 == 0 }

    >>> even_set

    set([8, 2, 4])

    >>> # Dict Comprehensions

    >>> d = { x: x % 2 == 0 for x in range(1, 11) }

    >>> d

    {1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False, 10: True}

在第一个例子里，我们以some_list为基础，创建了一个具有不重复元素的集合，而且集合里只包含偶数。而在字典表的例子里，我们创建了一个key是不重复的1到10之间的整数，value是布尔型，用来指示key是否是偶数。

这里另外一个值得注意的事情是集合的字面量表示法。我们可以简单的用这种方法创建一个集合：

    >>> my_set = {1, 2, 1, 2, 3, 4}

    >>> my_set

    set([1, 2, 3, 4])

而不需要使用内置函数set()。

##2. 计数时使用Counter计数对象。

这听起来显而易见，但经常被人忘记。对于大多数程序员来说，数一个东西是一项很常见的任务，而且在大多数情况下并不是很有挑战性的事情——这里有几种方法能更简单的完成这种任务。

Python的collections类库里有个内置的dict类的子类，是专门来干这种事情的：

    >>> from collections import Counter

    >>> c = Counter('hello world')

    >>> c

    Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

    >>> c.most_common(2)

    [('l', 3), ('o', 2)]


##3. 漂亮的打印出JSON

JSON是一种非常好的数据序列化的形式，被如今的各种API和web service大量的使用。使用python内置的json处理，可以使JSON串具有一定的可读性，但当遇到大型数据时，它表现成一个很长的、连续的一行时，人的肉眼就很难观看了。

为了能让JSON数据表现的更友好，我们可以使用indent参数来输出漂亮的JSON。当在控制台交互式编程或做日志时，这尤其有用：

    >>> import json

    >>> print(json.dumps(data))  # No indention

    {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": false}]}

    >>> print(json.dumps(data, indent=2))  # With indention

    {

     "status": "OK",

     "count": 2,

     "results": [

       {

         "age": 27,

         "name": "Oz",

         "lactose_intolerant": true

       },

       {

         "age": 29,

         "name": "Joe",

         "lactose_intolerant": false

       }

     ]

    }

同样，使用内置的pprint模块，也可以让其它任何东西打印输出的更漂亮。

##4. 创建一次性的、快速的小型web服务

有时候，我们需要在两台机器或服务之间做一些简便的、很基础的RPC之类的交互。我们希望用一种简单的方式使用B程序调用A程序里的一个方法——有时是在另一台机器上。仅内部使用。

我并不鼓励将这里介绍的方法用在非内部的、一次性的编程中。我们可以使用一种叫做XML-RPC的协议 (相对应的是这个Python库)，来做这种事情。

下面是一个使用SimpleXMLRPCServer模块建立一个快速的小的文件读取服务器的例子：

    from SimpleXMLRPCServer import SimpleXMLRPCServer

    def file_reader(file_name):

       with open(file_name, 'r') as f:

           return f.read()

    server = SimpleXMLRPCServer(('localhost', 8000))

    server.register_introspection_functions()

    server.register_function(file_reader)

    server.serve_forever()

客户端：

    import xmlrpclib

    proxy = xmlrpclib.ServerProxy('http://localhost:8000/')

    proxy.file_reader('/tmp/secret.txt')

我们这样就得到了一个远程文件读取工具，没有外部的依赖，只有几句代码(当然，没有任何安全措施，所以只可以在家里这样做)。

##5. Python神奇的开源社区

这里我提到的几个东西都是Python标准库里的，如果你安装了Python，你就已经可以这样使用了。而对于很多其它类型的任务，这里有大量的社区维护的第三方库可供你使用。

下面这个清单是我认为的好用且健壮的开源库的必备条件：

好的开源库必须…

    包含一个很清楚的许可声明，能适用于你的使用场景。

    开发和维护工作很活跃(或，你能参与开发维护它。)

    能够简单的使用pip安装或反复部署。

    有测试套件，具有足够的测试覆盖率。

如果你发现一个好的程序库，符合你的要求，不要不好意思————大部分的开源项目都欢迎捐赠代码和欢迎提供帮助——即使你不是一个Python高手。
