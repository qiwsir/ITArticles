#Python特殊语法：filter、map、reduce、lambda、yield

Python内置了一些非常有趣但非常有用的函数，充分体现了Python的语言魅力！

##filter

filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：

    >>> def f(x): return x % 2 != 0 and x % 3 != 0

    >>> filter(f, range(2, 25))

    [5, 7, 11, 13, 17, 19, 23]

    >>> def f(x): return x != 'a'

    >>> filter(f, "abcdef")

    'bcdef'
##map

map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：

    >>> def cube(x): return x*x*x
    >>> map(cube, range(1, 11))
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    >>> def cube(x) : return x + x ...
    >>> map(cube , "abcde")
    ['aa', 'bb', 'cc', 'dd', 'ee']

另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：

    >>> def add(x, y): return x+y
    >>> map(add, range(8), range(8))
    [0, 2, 4, 6, 8, 10, 12, 14]

##reduce

reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：

    >>> def add(x,y): return x + y
    >>> reduce(add, range(1, 11))
    55
    （注：1+2+3+4+5+6+7+8+9+10）
    >>> reduce(add, range(1, 11), 20)
    75
    （注：1+2+3+4+5+6+7+8+9+10+20）

##lambda

lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方：

    >>> g = lambda x: x * 2
    >>> g(3)
    6
    >>> (lambda x: x * 2)(3)
    6

##yield

generator归根到底是一个函数的返回值，这个函数是包含“yield”关键字的python函数。

是不是可以这么说(不是很确定，似乎可以这么理解)

1. 凡包含“yield”关键字的函数，都返回generator
2. generator不是函数，而是函数执行后构造的对象，是一种iterator。
3. generator可以像iterator一样的用。

generator的根源是PEP 255，其中列出了generator在Python存在的原因，简单的讲，Generator在需要时返回中间值，能够保存当前的状态，等待下一次的返回要求。

xrange/range的区别或许可以帮我们理解这一点，xrange之所以存在，是因为range需要一次完成列表的初始化，存储等等，从C的角度来理解，就是，用range等于先malloc足够的内存，然后完成值的准备，等待调用(遍历等等)。而xrange则不这么干，什么时候要的时候，什么时候给值。所以，在Python 2.x中，type(range(10))是一个List，是内存中的静态数据；而type(xrange(10))则是一个range type。

到Python 3.x，xrange彻底替代了range函数。

这样设计的目的无非就是节省内存 ，千八百数字的无所谓，但ython 2.x的long int和Python 3.x的Int是无限制(用官方语言来说就是可以占满内存)。

generator为了满足这种需求设计的，状态得到了保存，随取随算。

PEP 255有一句： a Python generator is a kind of Python iterator[1], but of an especially powerful kind.

Python的产生器就是一种迭代器...

因为它是一种迭代器，所以，他可以用到for等控制流中。

    def gen():
        print "one"
        yield 1
        print "two"
        yield 2
        print "three"
        yield 3
    type(gen)
    type(gen())

可以看到gen是函数，而gen()是generator，应该说，函数gen执行的返回值是生成一个generator。

generator的方法之一就是next()。

    a=gen()
    a.next()
    a.next()
    a.next()
    a.next()

三次next，分别返回了1,2,3，最后一次，已到达末尾，发生StopIteration错误。

而yield的作用就是，每次发生next()调用，函数执行完yield语句之后在挂起，这时返回yield的值(你原因yield啥就yield啥)，整个函数状态被保存，等待下一次next()调用； 下次next()调用发生时，从yield后的语句开始执行(有yiled也在循环体内，未必一定是顺序的)，直到再次遇到yield为止，然后重复删除动作。

yield 可以解读为"返回然后等待"。知道所有yield语句完成，这时如果再次调用next()，则发生StopIteration异常，当然，在for循环之类的语句中会被自动处理。


来源：   http://blog.csdn.net/wanghai__/article/details/6936633 


