#! /usr/bin/env python
#coding:UTF-8

import random
i=0 
while i < 4:
    print'********************************'
    num = input('请您输入0到9任一个数：')
            
    xnum = random.randint(0,9)

    x = 3 - i 
      
    if num == xnum:
        print'运气真好，您猜对了！' 
        break 
    elif num > xnum:
        print'''您猜大了!\n哈哈,正确答案是:%s\n您还有%s次机会！''' %(xnum,x)
    elif num < xnum:
        print'''您猜小了!\n哈哈,正确答案是:%s\n您还有%s次机会！''' %(xnum,x)
    print'********************************'
    i += 1

"""
此代码是一个名曰李航的大学生发给我的，我用在了教程中
"""
