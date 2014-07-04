#random随机数生成

##random.random

random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0

##random.uniform

random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b。

    print random.uniform(10, 20)
    print random.uniform(20, 10)
    #---- 结果（不同机器上的结果不一样）
    #18.7356606526
    #12.5798298022  

random.randint

random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

    print random.randint(12, 20)          #生成的随机数n: 12 <= n <= 20
    print random.randint(20, 20)          #结果永远是20
    #print random.randint(20, 10)       #该语句是错误的。下限必须小于上限。  

##random.randrange

random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。如：

random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。

##random.choice

random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章，也可以参考：http://www.17xie.com/read-37422.html 。下面是使用choice的一些例子：

    print random.choice("学习Python")
    print random.choice(["JGood", "is", "a", "handsome", "boy"])
    print random.choice(("Tuple", "List", "Dict"))  

##random.shuffle

random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。如:

    p = ["Python", "is", "powerful", "simple", "and so on..."]
    random.shuffle(p)
    print p
    #---- 结果（不同机器上的结果可能不一样。）
    #['powerful', 'simple', 'is', 'Python', 'and so on...']  

##random.sample

random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice = random.sample(list, 5)
    #从list中随机获取5个元素，作为一个片断返回
    print slice
    print list                         #原有序列并没有改变。    　　

上面这些方法是random模块中最常用的，在Python手册中，还介绍其他的方法。感兴趣的朋友可以通过查询Python手册了解更详细的信息。


来源：   http://blog.csdn.net/JGood/article/details/4278885 
