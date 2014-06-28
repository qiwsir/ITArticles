#关键字yield的解释

原文地址：http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

译者注:这是stackoverflow上一个很热的帖子，这里是投票最高的一个答案。

##提问者的问题

Python关键字yield的作用是什么？用来干什么的？

比如，我正在试图理解下面的代码:

    def node._get_child_candidates(self, distance, min_dist, max_dist):
        if self._leftchild and distance - max_dist < self._median:
            yield self._leftchild
        if self._rightchild and distance + max_dist >= self._median:
            yield self._rightchild

下面的是调用:

    result, candidates = list(),[self]while candidates:
        node = candidates.pop()
        distance = node._get_dist(obj)if distance <= max_dist and distance >= min_dist:
            result.extend(node._values)
        candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))return result

当调用 _get_child_candidates 的时候发生了什么？返回了一个链表？返回了一个元素？被重复调用了么？ 什么时候这个调用结束呢？
理解yield工作过程编辑本段回目录

（注：这是此问题的第一个回答，也是受关注最高的）

为了理解什么是 yield,你必须理解什么是生成器。在理解生成器之前，让我们先走近迭代。

###可迭代对象

当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:

    >>> mylist=[1,2,3]
    >>> for i in mylist:
    ... print(i)
    1
    2
    3

mylist 是一个可迭代的对象。当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:

    >>> mylist=[x*x for x in range(3)]
    >>> for i in mylist:
    ...     print(i)
    0
    1
    4
    
所有你可以使用 for..in.. 语法的叫做一个迭代器:链表，字符串，文件... 你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

###生成器

生成器是可以跌代的，但是你**只可以读取它一次**,因为它并不把所有的值放在内存中，它是实时地生成数据:

    >>> mygenerator=(x*x for x in range(3))
    >>> for i in mygenerator:
    ...     print(i)
    0
    1
    4

看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator , 因为生成器只能被迭代一次:先计算出0,然后继续计算1,然后计算4,一个跟一个的..

###yield关键字

yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

    >>> def createGenerator():
    ... mylist=range(3)
    ... for i in mylist:
    ...     yield i*i
    ...
    >>>mygenerator=createGenerator()    # create a generator
    >>> print(mygenerator)              # mygenerator is an object!
    <generator object createGenerator at 0xb7555c34>
    >>> for i in mygenerator:
    ... print(i)
    0
    1
    4

这个例子没什么用途，但是它让你知道，这个函数会返回一大批你只需要读一次的值.

为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

现在到了关键点了！

第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。

##回到你的代码

(译者注:这是回答者对问题的具体解释)

###生成器:

    # Here you create the method of the node object that will return the generator
    
    def node._get_child_candidates(self, distance, min_dist, max_dist):

        # Here is the code that will be called each time you use the generator object :

        # If there is still a child of the node object on its left
        # AND if distance is ok, return the next child

        if self._leftchild and distance - max_dist < self._median:
            yield self._leftchild

        # If there is still a child of the node object on its right
        # AND if distance is ok, return the next child
        if self._rightchild and distance + max_dist >= self._median:
                yield self._rightchild

        # If the function arrives here, the generator will be considered empty
        # there is no more than two values : the left and the right children

调用者:

    # Create an empty list and a list with the current object reference
    result,candidates=list(),[self]
    # Loop on candidates (they contain only one element at the beginning)
    while candidates:
        # Get the last candidate and remove it from the list
        node=candidates.pop()
        # Get the distance between obj and the candidate
        distance=node._get_dist(obj)
        # If distance is ok, then you can fill the result
    if distance <= max_dist and distance>=min_dist:
        result.extend(node._values)
    # Add the children of the candidate in the candidates list
    # so the loop will keep running until it will have looked
    # at all the children of the children of the children, etc. of the candidate
        candidates.extend(node._get_child_candidates(distance,min_dist,max_dist))
    return result

这个代码包含了几个小部分：

- 我们对一个链表进行迭代，但是迭代中链表还在不断的扩展。它是一个迭代这些嵌套的数据的简洁方式，即使这样有点危险，因为可能导致无限迭代。 candidates.extend(node._get_child_candidates(distance,min_dist,max_dist)) 穷尽了生成器的所有值，但 while 不断地在产生新的生成器，它们会产生和上一次不一样的值，既然没有作用到同一个节点上.
- extend() 是一个迭代器方法，作用于迭代器，并把参数追加到迭代器的后面。

通常我们传给它一个链表参数:

    >>> a=[1,2]
    >>> b=[3,4]
    >>> a.extend(b)
    >>> print(a)
    [1, 2, 3, 4]

但是在你的代码中的是一个生成器，这是不错的，因为：

- 你不必读两次所有的值
- 你可以有很多子对象，但不必叫他们都存储在内存里面。

并且这很奏效，因为Python不关心一个方法的参数是不是个链表。Python只希望它是个可以迭代的，所以这个参数可以是链表，元组，字符串，生成器... 这叫做 ducktyping,这也是为何Python如此棒的原因之一，但这已经是另外一个问题了...

你可以在这里停下，来看看生成器的一些高级用法:

###控制生成器的穷尽

    >>> classBank():# let's create a bank, building ATMs
        ... crisis=False
    ... defcreate_atm(self):
        ... whilenotself.crisis:
            ... yield"$100"
    >>> hsbc=Bank()# when everything's ok the ATM gives you as much as you want
    >>> corner_street_atm=hsbc.create_atm()
    >>> print(corner_street_atm.next())
    $100
    >>> print(corner_street_atm.next())
    $100
    >>> print([corner_street_atm.next()forcashinrange(5)])
    ['$100', '$100', '$100', '$100', '$100']
    >>> hsbc.crisis=True# crisis is coming, no more money!
    >>> print(corner_street_atm.next())
    <type 'exceptions.StopIteration'>
    >>> wall_street_atm=hsbc.create_atm()# it's even true for new ATMs
    >>> print(wall_street_atm.next())
    <type 'exceptions.StopIteration'>
    >>> hsbc.crisis=False# trouble is, even post-crisis the ATM remains empty
    >>> print(corner_street_atm.next())
    <type 'exceptions.StopIteration'>
    >>> brand_new_atm=hsbc.create_atm()# build a new one to get back in business
    >>> forcashinbrand_new_atm:
    ... print cash
    $100
    $100
    $100
    $100
    $100
    $100
    $100
    $100
    $100...

对于控制一些资源的访问来说这很有用。

###Itertools,你最好的朋友

itertools包含了很多特殊的迭代方法。是不是曾想过复制一个迭代器?串联两个迭代器？把嵌套的链表分组？不用创造一个新的链表的 zip/map?

只要 import itertools

需要个例子？让我们看看比赛中4匹马可能到达终点的先后顺序的可能情况:

    >>> horses=[1,2,3,4]
    >>> races=itertools.permutations(horses)
    >>> print(races)
    <itertools.permutations object at 0xb754f1dc>
    >>> print(list(itertools.permutations(horses)))
    [(1, 2, 3, 4),
    (1, 2, 4, 3),
    (1, 3, 2, 4),
    (1, 3, 4, 2),
    (1, 4, 2, 3),
    (1, 4, 3, 2),
    (2, 1, 3, 4),
    (2, 1, 4, 3),
    (2, 3, 1, 4),
    (2, 3, 4, 1),
    (2, 4, 1, 3),   
    (2, 4, 3, 1),
    (3, 1, 2, 4),
    (3, 1, 4, 2),
    (3, 2, 1, 4),
    (3, 2, 4, 1),
    (3, 4, 1, 2),
    (3, 4, 2, 1),
    (4, 1, 2, 3),
    (4, 1, 3, 2),
    (4, 2, 1, 3),
    (4, 2, 3, 1),
    (4, 3, 1, 2),
    (4, 3, 2, 1)]

###了解迭代器的内部机理

迭代是一个实现可迭代对象(实现的是 __iter__() 方法)和迭代器(实现的是 __next__() 方法)的过程。可迭代对象是你可以从其获取到一个迭代器的任一对象。迭代器是那些允许你迭代可迭代对象的对象。

更多见这个文章 http://effbot.org/zone/python-for-statement.htm

（以上翻译来自：https://pyzh.readthedocs.org/en/latest/the-python-yield-keyword-explained.html）

##迅速理解 yield内核

当你遇到有yield语句的函数时，尝试用下面的方式追踪其过程，从而理解内部运行机理：

- 在函数的开始处插入一行 result = [] .
- 将每个 yield expr的表达式用 result.append(expr)替换.
- 在函数的末尾插入一行 return result .
- 很好，再没有yield语句了。运行代码吧。
- 最后还要将整个函数回复原状.

这个技巧能够让你理解函数背后的逻辑过程，但是，yield中真正发生的和列表中所发生的是有显著差别的。很多情况中，yield方法会更有效和快速。此外，如果赶上你倒霉，上面的过程会让你陷入死循环，当然原来的函数是正常工作的。

###不要拒绝迭代——迭代器和生成器

首先，迭代器的样式：

    for x in mylist:
    ...loop body...

对此，Python执行以下两步：

1. 为 mylist构造一个迭代器:
2. 调用 iter(mylist) -> 用 next()方法得到一个返回对象 (如果在Python 3中，则是 __next__() ).

**[这一步是很多人都不告诉你的。]**

用迭代器循环:

- 在迭代器中不断调用 next() 方法，执行第一步，得到返回对象。不断地在循环体中得到next()的返回值，并赋给一个变量x.如果next()抛出了 StopIteration 异常，就意味着迭代器不再有值输出，并且退出循环。

事实上，Python在针对任何一个对象内容进行循环的时候，都要执行上述两步，所以它实质是一个循环，但是它也是类似otherlist.extend(mylist)(otherlist是一个列表）过程。

列表mylist是可迭代的，因为它执行迭代器协议。在class中，你能够执行__iter__()方法，让类实例可迭代。这种方法应该返回一个迭代器。一个迭代器是带有next()方法的对象，它也可能在同一个类中分别执行__iter__()和next()，__iter__()返回self。这是简单情况，但是，你不能奢望在同一时刻同一个对象中运行两个迭代器循环。

这就是迭代器协议，很多对象多执行这个协议，例如:

    内建列表、字典、元组、集合、文件.
    自定义类中的 __iter__().
    生成器.

注意，for循环不知道正在处理的对象——它随从于迭代器，并且在调用next()的时候得到结果。内建列表一个一个地返回结果，字典也按照关键词逐个返回，文件则逐个返回行。生成器就涉及到yield了

    def f123():
        yield1
        yield2
        yield3
    for item in f123():
        print item

不用yield语句，如果在 f123() 函数中有三个 return语句，那么将只有第一个得到执行后函数即退出，但这不是本意。如果用yield，函数 f123() 被调用，它返回的不是值，而是生成器对象。也可说函数没有真的退出，它进入了休息状态，当用for 循环读取生成器的时候，才再次被唤醒并执行，直到下一个yield语句，并返回下一个项目。这个过程发生在函数退出之前，拐点就是生成器抛出StopIteration异常和退出循环。

所以，生成器对象就像一种编辑器，一方面它是通过__iter__()和next()方法，借助for循环迭代的结果，另外一方面，它可以在函数运行过程中获得各个输出值，并把这些值存在缓存中。

###為什麼用生成器?

通常你不用生成器，但是这仅限于简单逻辑，用临时列表就解决问题了。但是不是所有情况都如此。比如，如果你面对一个无限循环，或者在处理一个很长的列表时使得内存低效，这时候的解决方法就是建立一个新的迭代类，在这里生成器就让问题简单了。

##拒绝yield的两个简单例子

The yield keyword is reduced to two simple facts:

If the compiler detects the yield keyword anywhere inside a function, that function no longer returns via the return statement. Instead, it immediately returns a lazy "pending list" object called a generator

A generator is iterable. What is an iterable? It's anything like a list or set or range or dict-view, with a built-in protocol for visiting each element in a certain order.

In a nutshell: a generator is a lazy, incrementally-pending list, and yield statements allow you to use function notation to program the list values the generator should incrementally spit out.

    generator = myYieldingFunction(...)
    x = list(generator)
    
       generator
           v
    [x[0],...,???]
    
             generator
                 v
    [x[0], x[1],...,???]

                   generator
                       v
    [x[0], x[1], x[2],...,???]StopIteration exception
    [x[0], x[1], x[2]]done

    list==[x[0], x[1], x[2]]
    
###Example
    
Let's define a function makeRange that's just like Python's range. Calling makeRange(n) RETURNS A GENERATOR:
    
    def makeRange(n):# return 0,1,2,...,n-1
        i =0while i < n:yield i
            i +=1>>> makeRange(5)<generator object makeRange at 0x19e4aa0>

To force the generator to immediately return its pending values, you can pass it into list() (just like you could any iterable):

    >>> list(makeRange(5))[0,1,2,3,4]

Comparing example to "just returning a list"

The above example can be thought of as merely creating a list which you append to and return:

    # list-version                   #  # generator-versiondef makeRange(n):#  def makeRange(n):"""return [0,1,2,...,n-1]"""#~          """return   0,1,2,...,n-1"""
        TO_RETURN =[]#>
        i =0#      i = 0while i < n:#      while i < n:
            TO_RETURN +=[i]#~         yield i
            i +=1#      i += 1return TO_RETURN             #>>>> makeRange(5)[0,1,2,3,4]

There is one major difference though; see the last section.

###How you might use generators

An iterable is the last part of a list comprehension, and all generators are iterable, so they're often used like so:

    #_ITERABLE_>>>[x+10for x in makeRange(5)][10,11,12,13,14]

To get a better feel for generators, you can play around with the itertools module (be sure to use chain.from_iterable rather than chain when warranted). For example, you might even use generators to implement infinitely-long lazy lists like itertools.count(). You could implement your own def enumerate(iterable): zip(count(), iterable), or alternatively do so with the yield keyword in a while-loop.

Please note: generators can actually be used for many more things, such as implementing coroutines or non-deterministic programming or other elegant things. However, the "lazy lists" viewpoint I present here is the most common use you will find.
Behind the scenes

This is how the "Python iteration protocol" works. That is, what is going on when you do list(makeRange(5)). This is what I describe earlier as a "lazy, incremental list".

    >>> x=iter(range(5))>>>next(x)0>>>next(x)1>>>next(x)2>>>next(x)3>>>next(x)4>>>next(x)Traceback(most recent call last):File"<stdin>", line 1,in<module>StopIteration

The built-in function next() just calls the objects .next() function, which is a part of the "iteration protocol" and is found on all iterators. You can manually use the next() function (and other parts of the iteration protocol) to implement fancy things, usually at the expense of readability, so try to avoid doing that...
Minutiae

Normally, most people would not care about the following distinctions and probably want to stop reading here.

In Python-speak, an iterable is any object which "understands the concept of a for-loop" like a list [1,2,3], and an iterator is a specific instance of the requested for-loop like [1,2,3].__iter__(). A generator is exactly the same as any iterator, except for the way it was written (with function syntax).

When you request an iterator from a list, it creates a new iterator. However, when you request an iterator from an iterator (which you would rarely do), it just gives you a copy of itself.

Thus, in the unlikely event that you are failing to do something like this...

    > x = myRange(5)> list(x)[0,1,2,3,4]> list(x)[]

... then remember that a generator is an iterator; that is, it is one-time-use. If you want to reuse it, you should call myRange(...) again. Those who absolutely need to clone a generator (for example, who are doing terrifyingly hackish metaprogramming) can use itertools.tee if absolutely necessary, since the copyable iterator Python PEP standards proposal has been deferred.

