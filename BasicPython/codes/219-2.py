#!/usr/bin/env python
#coding:utf-8

class A:
    def __init__(self):
        print "aaa"

class B(A):
    pass

if __name__=="__main__":
    a = A()
    b = B()
