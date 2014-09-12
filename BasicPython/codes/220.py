#!/usr/bin/env python
#coding:utf-8

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class Programmer(Person):
    def __init__(self, name,email,lang, system, website):
        Person.__init__(self,name,email)
        self.lang = lang
        self.system = system
        self.website = website

class Pythoner(Programmer):
    def __init__(self,name,email):
        Programmer.__init__(self,name,email,"python","Ubuntu","qiwsir.github.io")

if __name__=="__main__":
    writer = Pythoner("qiwsir","qiwsir@gmail.com")
    print "name=",writer.name
    print "lang=",writer.lang
    print "email=",writer.email
    print "system=",writer.system
    print "website=",writer.website
