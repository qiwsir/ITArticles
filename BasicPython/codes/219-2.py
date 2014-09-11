#!/usr/bin/env python
#coding:utf-8

class A:
    def __init__(self):
        print "aaa"

class B(A):
    def __init__(self):
        #print "bbb"
        A.__init__(self)

if __name__=="__main__":
    a = A()
    b = B()
