#!/usr/bin/env python
#coding:utf-8

class A:
    def __init__(self):
        print "aaa"
    def amethod(self):
        print "method a"

class B(A):
    def __init__(self):
        print "bbb"


if __name__=="__main__":
    print "A--->"
    a = A()
    a.amethod()
    print "B--->"
    b = B()
    b.amethod()
