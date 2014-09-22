#!/usr/bin/env python
#coding:utf-8

class Person:
    def __init__(self,name):
        self.name = name
        print self.name

    def __work(self,salary):
        print "%s salary is: %d"%(self.name,salary)

    def worker(self):
        self.__work(500)

if __name__=="__main__":
    officer = Person("Tom")
    #officer.__work(1000)
    officer.worker()
    
