#!/usr/bin/env python
#coding:utf-8

import random

number = random.randint(1,100)

print "请输入一个100以内的自然数："

input_number = raw_input()

if number == int(input_number):
    print "猜对了，这个数是："
    print number
elif number > int(input_number):
    print "小了"
    input_number = raw_input()
elif number < int(input_number):
    print "大了"
    input_number = raw_input()
else:
    print "错了。"
