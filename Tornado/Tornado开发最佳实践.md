#Tornado开发最佳实践

最近看到很多人的开发经验. 比如ruby和rails的使用者非常喜欢传道授业解惑, 网上能看到的python的文章大多数在研究一些好玩的算法等等. 事实上python在顶级软件团队的应用程度相当普遍, 在严肃的生产环境中也十分让人放心. 只是几乎所有的python framework都不擅长宣传自己, 本人有一次一口气浏览了大部分python web框架的主页, 没有一个框架主页有视频教程. 相比rails甚至Java的play framework首页都有screencast.

在干活方面我是一个非常不主流的人, 大家都在谈论的的rails我不用, 一心放在python的framework tornado上, 即使很多用python的人也多在使用django这些流行的框架, 但是我的tornado却越用越顺手, 几乎形成了一套最佳开发实践, 完成项目的速度连我自己都吓了一跳. 本文介绍自己的经验, 顺便对其他传言迎头痛击.
没有ORM的框架不用也罢？

我完全不同意. tornado没有ORM, 2.x自带了一个模块database.py, 开始接触tornado的时候我想也没想就用了, 初看它是一个对mysql-python的简单包装而已, 我也对database.py存在的必要性表示过质疑. 但是慢慢我发现这个模块很好用, 也很必要. 这个模块独立于tornado, 偶尔将database.py单独拿出来放到其他的项目里, 现在已经离不开了.

这里再多说两句, 直接使用mysql-python看似也没有多大的差别, 但是返回的数据往往都是各种object. 使用python的话我们更加习惯返回的东西是字典和列表. database.py 就帮我们完成了这步, 基本做到了写SQL直接返回字典/列表的对象. 常用的方法只有get, query 和 execute 三种, 对应了结果只有一行数据, 多行数据, 以及无需返回数据的三种数据库查询 (其中execute还有两种, 一个返回插入数据行的id, 一个返回SQL执行影响的行数). 使用database.py 另外一个好处也就是能减少SQL注入的风险.

果不其然, 在tornado 3.x里面, 这个模块被独立了出来, 变成了torndb这 个独立的库. 这是个好事, 首先是tornado变成一个更加纯web的东西, 数据库相关的功能被剥离, 变瘦了, 越来越胖的rails就没那么帅了, 人到中年都要注意体重问题, 对不对DHH? 另外torndb也可以被利用在各种项目里, 我猜一定是有很多人以前和我一样单独拿database.py出来在其他项目里面用, 所以独立了则更加方便了.

不使用ORM有各种好处, 首先编程人员需要自己写出SQL, 这个是基础, 连这个都怕? 直接面对问题才能消灭恐惧感. 自己写SQL可以直接复制粘贴在MySQL里面看结果, 另外也不太容易写出性能超低的SQL语句: 如果你自己写的SQL都觉得恶心, 你还会提交在代码里面吗?

所以我是反ORM派别的, torndb是一个非常轻量级别的包装, 非常的适度, 推荐使用. 形成这些思想主要原因是, 早年受到大牛Bob Ippolito (@etrepum) 的一些指点, 此人最出名的就是写了simplejson, 当年他跟我说他们用SQLAlchemy但是从来不用ORM部分, 要求全部程序员手写RAW SQL.
第二, 我们都希望我们自己用的框架是全功能的

比如长链接, 即时的web应用, 现在是越来越常见了. 在这个领域没有太多解决方案, node.js和tornado就是其中最好的两个.

一般ruby开发者会借助node.js来实现长链接(比如yammer). 而python开发者, 如果之前没有使用tornado, 一般会通过tornado来实现长链接(比如quora). 直接基于tornado的项目(比如知乎)就不需要使用混合架构了, 减少了系统依赖组件的数量是一个很好的事情, 再不济也省了内存.
第三, 我们谈mobile兼容的架构

现在的网站全部要考虑mobile API, 也就是说原来的AJAX现在要向API靠拢, 争取一个API, web和mobile都能用. 原来的AJAX本来是需要渲染html的, 现在改造成API返回数据就全部变成JSON, 我的项目都是这么做的.

Tornado对于前端完全不管, 不像rails这样的框架则是什么都管. 在前端方面必须要用的组件: coffee-script, underscore.js, jQuery

coffee-script让你用一种ruby和python混合的语法(coffee)来写js, 极大的缩短代码行数. 由于写js里面回调太多(异步代码风格), 使用coffee会极大提升你的编码效率.

underscore.js本身也是对JS语言(数据结构)的一种扩 充, 另外underscore.js提供一个模版系统, 正好和jquery的功能相互补充. 我前面提到的用JS调用API并且渲染成DOM的关键组件, 就是这个underscore.js提供的JS模版功能, JSON的数据很容易的转换成DOM然后用jquery插入到网页中. 另外如果你们去npm看一看, 会发现underscore.js是一个比jQuery地位还要重要的组件, 原因我已经说过了, underscore.js是对JS语言级别的补充, 这里强调一下, 这个库是在用node写后端的时候也可以用的, 写node后端的时候基本上可不会用到jQuery.

jQuery不用说了, DOM操作, AJAX都是常用的功能. 另外还有一堆插件依赖jQuery.

采用了这种架构, 写web app就是在狂写coffee, 从API取得数据然后做大量的DOM操作. 当然我们在写iOS和Android的时候, 这些API都是可以被重用的. 唯一的问题在SEO上, 为了解决这个问题, 在某些用户无需Login的页面, 我们还是要用传统的方法将数据渲染到html里面以供搜索引擎收录.
第四, 接下来我们谈谈大数据的处理

这套架构在处理大流量的时候, 自然的需要利用memcache或者redis来做一些缓存. 但是更大的数据就不仅仅是cache就有用了, 一般需要shard, 在这方面我做利用MySQL来做NoSQL的事情, 并且我自己写了一个开源的东西NoMagic, 理论依据是根据tornado老大(Bret Taylor, 前Facebook CTO, 够NB吧)的一篇博客http://backchannel.org/blog/friendfeed-schemaless-mysql. 根据性能需要, 我们有可能会用某些其他的引擎来代替MySQL来做存储. 如果你理解一个数据库实际上是索引和存储两个事情的结合, 那么你会很轻易的掌握这部分的奥妙.

在编程模型方面, 面对真正的大数据, 你需要的将基于查询的数据库操作变成K/V的操作. 简单的来说, 原来你需要在所有的post里面找到这个用户id的贴子, 现在变成了你知道这个用户创建的帖子一共有哪些(id), 一次性的找出来(SELECT IN 操作).

这些技术表示我们在面对海量数据的时候不是没有工具可用, 但是编码是艰苦的. 当你真的有那么大的数据或者用户量的时候, 在编程上多花点时间似乎不算浪费.
最后的秘密武器

我以前不是很重视, 但是现在越来越看重, 就是TDD.

TDD不是强迫大家使用的, 对于简单的逻辑, TDD可能是浪费(时间)的. 但是如果你的项目不是外包性质的话, 那么会有一天原来简单的API就变复杂化了, 或者说测试逻辑开始复杂话了.

我的建议是, 当你觉得测试效率开始降低的时候, 开始你的自动化测试之旅. 这些原因可能包括: 测试的逻辑变得复杂, 测试的环境变得复杂(比如一个web项目的测试需要动用手机+Xcode), 以及重复性测试. 将测试代码化要好于文档化.

如何开始自动化测试, 其实很简单, 假设你现在一无所有, 那么每修复一条bug的时候, 增加一条测试用例. 这个经验来自最近LinkedIn提倡的持续发布开发方法, 应该是持续集成方法的延续. 个人不是很喜欢敏捷这样的说法, 因为这个概念已经太老了.
关于测试

我们是用到tornado的testing的, 它还是基于python, 是对python unittest的增强(tornado的很多组件都使得原来的系统更加好用了). 如果你有一个团队, 还可以考虑buildbot来将所有的测试自动化, 分布式. 我在这里讲的每一个线索都需要花一定时间研究, 研究buildbot是很需要勇气的, 但是一旦掌握威力也是巨大的.

基于tornado的工具链是一个互联网/移动互联网的专业团队的利器, 这个世界上有很多的纯python团队(除了必须要用的js, objc, java4android以外)在自动化和专业化方向做到了惊人的高度. 他们在解决各种问题的时候必然使用了更多的工具, 注入了更多的智慧.
题外话

很多团队还有对搜索的需求, 我比较推荐 sphinx, 似乎对中文的支持也有.
总结

整个工具链包括 ubuntu LTS, nginx, python 2.7, tornado, torndb, buildbot, coffee-script, underscore.js, jQuery, MySQL, memcache, redis, memcachedb, sphinx. 一个相当明显的特点就是这里面尽量避免了和Java有关的一切技术, 比如我们选择了buildbot而不是更加流行的jenkins, 选择了sphinx而不是基于Java的Lucene. 现在除了Android不得不用Java写以外, 其他的都可以绕过. 不是C就是python. 我不排除这个世界上有很多更加神奇的团队已经迈入函数式语言解决实际问题的境界, 对于这些团队我表示无限敬仰. 另外我们也绕过了流行但是让人看不懂的东西比如mongodb以及cassandra, 我们更加倾向于一句话就能讲清原理的东西比如redis和memcache.
开发环境

推荐MacBook Air, 一定要8G内存定制, 开发工具以简单sublime text 2和vim为主, 也是要求大家练就一身硬功夫. 顺便开一些虚拟机virtualbox测试用.

本文没有涉及到的东西也很多, 比如用python做一些统计方面的工作, 在商业决策支持上的应用, 等等. 学海无涯, 不断进步.

来源：http://simple-is-better.com/news/997

