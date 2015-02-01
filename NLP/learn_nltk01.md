www.nltk.org

    import nltk
    nltk.download()     #download the book in nltk

    from nltk.book import *
    # there are some book, like :
    >>> from nltk.book import *
    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908)')

    >>> text1.concordance("monstrous"))     #查询文本中的词汇，并列出上下文

##问题

>>> text1.similar("good")) 疑问：是不是查询出与good的上下文结构相似的词汇？即得到的词汇上下文和'good'相似。如果是这样，那么这里的上下文是按照什么标准定义为相似？

    >>> fdist1 = FreqDist(text1)    #找出文本中最常见的50个词汇。结果是类似dict类型的数据. 我怀疑是默认列出前50个
    >>> fdist1
    FreqDist({u',': 18713, u'the': 13721, u'.': 6862, u'of': 6536, u'and': 6024, u'a': 4569, u'to': 4542, u';': 4072, u'in': 3916, u'that': 2982, ...})

    >>> fdist1.hapaxes()   #列出只出现一次的词汇

nltk频率分布类中定义的函数

|例子|描述|
|---|-----|
|fdist=FreqDist(samples)|创建包含给定样本的频率分布|
|fdist.inc(sample)|增加样本|
|fdist['monstrous']|给定样本出现的次数|
|fdist.freq('monstrous')|给定样本的频率|
|fdist.N()|样本总数|
|fdist.keys()|以频率递减的样本list|
|for sample in fdist:|以频率递减遍历样本|
|fdist.max()|数值最大的样本|
|fdist.tabulate()|绘制频率分布表|
|fdist.plot()|绘制频率分布图|
|fdist.plot(cumulative=Ture)|绘制累积频率分布图|
|fdist1 < fdist2|测试样本在fdist1中出现的频率是否小于fdist2|



