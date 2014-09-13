#!/usr/bin/env python
#coding:utf-8

def outer_foo():
    a = 10
    def inner_foo():
        a = 20
        print "inner_foo,a=",a
    
    inner_foo()
    print "outer_foo,a=",a

a = 30
outer_foo()
print "a=",a
