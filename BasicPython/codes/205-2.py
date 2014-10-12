
"""
       This is a game.
       I am Qiwei.
       I like python.
       I am writing python articles in my website.
       My website is http://qiwsir.github.io
       You can learn python free in it.
"""

#!/usr/bin/env python
#coding:utf-8

import random

number = random.randint(1,100)

guess = 0

while True:

    num_input = raw_input("please input one integer that is in 1 to 100:")
    guess +=1

    if not num_input.isdigit():
        print "Please input interger."
    elif int(num_input)<0 or int(num_input)>=100:
        print "The number should be in 1 to 100."
    else:
        if number==int(num_input):
            print "OK, you are good.It is only %d, then you successed."%guess
            break
        elif number>int(num_input):
            print "your number is more less."
        elif number<int(num_input):
            print "your number is bigger."
        else:
            print "There is something bad, I will not work"
