#! /usr/bin/env python
#coding:utf-8

print "请输入字符串,然后按下回车键："

user_input = raw_input()

result = user_input.isdigit()

if not result:
    print "您输入的不完全是数字"

elif int(user_input)%2==0:
    print "您输入的是一个偶数"
elif int(user_input)%2!=0:
    print "您输入的是一个奇数"
else:
    print "您没有输入什么呢吧"
