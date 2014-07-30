#Python开发注意事项

这篇文章收集了我在Python新手开发者写的代码中所见到的不规范但偶尔又很微妙的问题。本文的目的是为了帮助那些新手开发者渡过写出丑陋的Python代码的阶段。为了照顾目标读者，本文做了一些简化（例如：在讨论迭代器的时候忽略了生成器和强大的迭代工具itertools）。

对于那些新手开发者，总有一些使用反模式的理由，我已经尝试在可能的地方给出了这些理由。但通常这些反模式会造成代码缺乏可读性、更容易出bug且不符合Python的代码风格。如果你想要寻找更多的相关介绍资料，我极力推荐The Python Tutorial或Dive into Python。

##迭代

###range的使用

Python编程新手喜欢使用range来实现简单的迭代，在迭代器的长度范围内来获取迭代器中的每一个元素：

    for i in range(len(alist)):
        print alist[i]

应该牢记：range并不是为了实现序列简单的迭代。相比那些用数字定义的for循环，虽然用range实现的for循环显得很自然，但是用在序列的迭代上却容易出bug，而且不如直接构造迭代器看上去清晰：

    for item in alist:
        print item

range的滥用容易造成意外的大小差一(off-by-one)错误，这通常是由于编程新手忘记了range生成的对象包括range的第一个参数而不包括第二个，类似于java中的substring和其他众多这种类型的函数。那些认为没有超出序列结尾的编程新手将会制造出bug：

    # 迭代整个序列错误的方法
    alist = ['her', 'name', 'is', 'rio']
    for i in range(0, len(alist) - 1): # 大小差一（Off by one）!
        print i, alist[i]

不恰当地使用range的常见理由：

1. 需要在循环中使用索引。这并不是一个合理的理由，可以用以下方式代替使用索引：

    for index, value in enumerate(alist):
        print index, value

2. 需要同时迭代两个循环，用同一个索引来获取两个值。这种情况下，可以用zip来实现：

    for word, number in zip(words, numbers):
        print word, number

3. 需要迭代序列的一部分。在这种情况下，仅需要迭代序列切片就可以实现，注意添加必要的注释注明用意：

    for word in words[1:]: # 不包括第一个元素
        print word

有一个例外：当你迭代一个很大的序列时，切片操作引起的开销就比较大。如果序列只有10个元素，就没有什么问题；但是如果有1000万个元素时，或者在一个性能敏感的内循环中进行切片操作时，开销就变得非常重要了。这种情况下可以考虑使用xrange代替range [1]。

在用来迭代序列之外，range的一个重要用法是当你真正想要生成一个数字序列而不是用来生成索引：

    # Print foo(x) for 0<=x<5
    for x in range(5):
        print foo(x)

###正确使用列表解析

如果你有像这样的一个循环：

    # An ugly, slow way to build a list
    words = ['her', 'name', 'is', 'rio']
    alist = []
    for word in words:
        alist.append(foo(word))

你可以使用列表解析来重写：

    words = ['her', 'name', 'is', 'rio']
    alist = [foo(word) for word in words]

为什么要这么做？一方面你避免了正确初始化列表可能带来的错误，另一方面，这样写代码让看起来很干净，整洁。对于那些有函数式编程背景的人来说，使用map函数可能感觉更熟悉，但是在我看来这种做法不太Python化。

其他的一些不使用列表解析的常见理由：

1. 需要循环嵌套。这个时候你可以嵌套整个列表解析，或者在列表解析中多行使用循环：

    words = ['her', 'name', 'is', 'rio']
    letters = []
    for word in words:
        for letter in word:
            letters.append(letter)

使用列表解析：

    words = ['her', 'name', 'is', 'rio']
    letters = [letter for word in words
                      for letter in word]

注意：在有多个循环的列表解析中，循环有同样的顺序就像你并没有使用列表解析一样。

2. 你在循环内部需要一个条件判断。你只需要把这个条件判断添加到列表解析中去：

    words = ['her', 'name', 'is', 'rio', '1', '2', '3']
    alpha_words = [word for word in words if isalpha(word)]

一个不使用列表解析的合理的理由是你在列表解析里不能使用异常处理。如果迭代中一些元素可能引起异常，你需要在列表解析中通过函数调用转移可能的异常处理，或者干脆不使用列表解析。

##性能缺陷

###在线性时间内检查内容

在语法上，检查list或者set/dict中是否包含某个元素表面上看起来没什么区别，但是表面之下却是截然不同的。如果你需要重复检查某个数据结构里是否包含某个元素，最好使用set来代替list。（如果你想把一个值和要检查的元素联系起来，可以使用dict；这样同样可以实现常数检查时间。）

    # 假设以list开始
    lyrics_list = ['her', 'name', 'is', 'rio']

    # 避免下面的写法
    words = make_wordlist() # 假设返回许多要测试的单词
    for word in words:
        if word in lyrics_list: # 线性检查时间
            print word, "is in the lyrics"

    # 最好这么写
    lyrics_set = set(lyrics_list) # 线性时间创建set
    words = make_wordlist() # 假设返回许多要测试的单词
    for word in words:
        if word in lyrics_set: # 常数检查时间
            print word, "is in the lyrics"

[译者注：Python中set的元素和dict的键值是可哈希的，因此查找起来时间复杂度为O(1)。]

应该记住：创建set引入的是一次性开销，创建过程将花费线性时间即使成员检查花费常数时间。因此如果你需要在循环里检查成员，最好先花时间创建set，因为你只需要创建一次。

##变量泄露

###循环

通常说来，在Python中，一个变量的作用域比你在其他语言里期望的要宽。例如：在Java中下面的代码将不能通过编译：

    // Get the index of the lowest-indexed item in the array
    // that is > maxValue
    for(int i = 0; i < y.length; i++) {
    if (y[i] > maxValue) {
        break;
        }
    }
    // i在这里出现不合法：不存在i
    processArray(y, i);

然而在Python中，同样的代码总会顺利执行且得到意料中的结果：

    for idx, value in enumerate(y):
        if value > max_value:
            break

    processList(y, idx)

这段代码将会正常运行，除非子y为空的情况下，此时，循环永远不会执行，而且processList函数的调用将会抛出NameError异常，因为idx没有定义。如果你使用Pylint代码检查工具，将会警告：使用可能没有定义的变量idx。

解决办法永远是显然的，可以在循环之前设置idx为一些特殊的值，这样你就知道如果循环永远没有执行的时候你将要寻找什么。这种模式叫做哨兵模式。那么什么值可以用来作为哨兵呢？在C语言时代或者更早，当int统治编程世界的时候，对于需要返回一个期望的错误结果的函数来说为通用的模式为返回-1。例如，当你想要返回列表中某一元素的索引值：

    def find_item(item, alist):
        # None比-1更加Python化
        result = -1
        for idx, other_item in enumerate(alist):
            if other_item == item:
                result = idx
                break

        return result

通常情况下，在Python里None是一个比较好的哨兵值，即使它不是一贯地被Python标准类型使用（例如：str.find [2]）

###外作用域

Python程序员新手经常喜欢把所有东西放到所谓的外作用域——python文件中不被代码块（例如函数或者类）包含的部分。外作用域相当于全局命名空间；为了这部分的讨论，你应该假设全局作用域的内容在单个Python文件的任何地方都是可以访问的。

对于定义整个模块都需要去访问的在文件顶部声明的常量，外作用域显得非常强大。给外作用域中的任何变量使用有特色的名字是明智的做法，例如，使用IN_ALL_CAPS 这个常量名。 这将不容易造成如下bug：

    import sys

    # See the bug in the function declaration?
    def print_file(filenam):
        """Print every line of a file."""
        with open(filename) as input_file:
            for line in input_file:
                print line.strip()

    if __name__ == "__main__":
        filename = sys.argv[1]
        print_file(filename)

如果你看的近一点，你将看到print_file函数的定义中用filenam命名参数名，但是函数体却引用的却是filename。然而，这个程序仍然可以运行得很好。为什么呢？在print_file函数里，当一个局部变量filename没有被找到时，下一步是在全局作用域中去寻找。由于print_file的调用在外作用域中(即使有缩进)，这里声明的filename对于print_file函数是可见的。

那么如何避免这样的错误呢？首先，在外作用域中不是IN_ALL_CAPS这样的全局变量就不要设置任何值[3]。参数解析最好交给main函数，因此函数中任何内部变量不在外作用域中存活。

这也提醒人们关注全局关键字global。如果你只是读取全局变量的值，你就不需要全局关键字global。你只有在想要改变全局变量名引用的对象时有使用global关键字的必要。你可以在这里获取更多相关信息this discussion of the global keyword on Stack Overflow。

##代码风格

###向PEP8致敬

PEP 8是Python代码的通用风格指南，你应该牢记在心并且尽可能去遵循它，尽管一些人有充分的理由不同意其中一些细小的风格，例如缩进的空格个数或使用空行。如果你不遵循PEP8，你应该有除“我只是不喜欢那样的风格”之外更好的理由。下边的风格指南都是从PEP8中摘取的，似乎是编程者经常需要牢记的。

###测试是否为空

如果你要检查一个容器类型（例如：列表，词典，集合）是否为空，只需要简单测试它而不是使用类似检查len(x)>0这样的方法：

    numbers = [-1, -2, -3]
    # This will be empty
    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        # Do something awesome

如果你想在其他地方保存positive_numbers是否为空的结果，可以使用bool(positive_number)作为结果保存；bool用来判断if条件判断语句的真值。

###测试是否为None

如前面所提到，None可以作为一个很好的哨兵值。那么如何检查它呢？

如果你明确的想要测试None，而不只是测试其他一些值为False的项（如空容器或者0），可以使用：

    if x is not None:
        # Do something with x

如果你使用None作为哨兵，这也是Python风格所期望的模式，例如在你想要区分None和0的时候。

如果你只是测试变量是否为一些有用的值，一个简单的if模式通常就够用了：

    if x:
        # Do something with x

例如：如果期望x是一个容器类型，但是x可能作另一个函数的返回结果值变为None，你应该立即考虑到这种情况。你需要留意是否改变了传给x的值，否则可能你认为True或0. 0是个有用的值，程序却不会按照你想要的方式执行。

译者注：

    [1] 在Python2.x 中 range生成的是list对象，xrange生成的则是range对象；Python 3.x 废除了xrange，range生成的统一为range对象，用list工厂函数可以显式生成list；
    [2] string.find(str)返回str在string中开始的索引值，如果不存在则返回-1；
    [3] 在外作用于中不要给函数中的局部变量名设置任何值，以防止函数内部调用局部变量时发生错误而调用外部作用域中的同名变量。

本文属翻译作品，英文原文标题是：Anti-Patterns in Python Programming。若无特别说明，英文原文及其衍生作品均使用知识共享署名-相同方式共享（Creative Commons）协议。您可以自由复制、散布、展示及演出本作品；若您改变、转变或更改本作品，仅在遵守与本作品相同的授权条款下，您才能散布由本作品产生的派生作品。

来源：http://www.techug.com/anti-patterns-in-python-programming
