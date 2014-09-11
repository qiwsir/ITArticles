#!/usr/bin/env python
#coding:utf-8

class Person:
    def __init__(self, name, lang, email):
        self.name = name
        self.lang = lang
        self.email = email
    
    def author(self):
        return self.name
"""
class Programmer:
    def __init__(self, name, lang, email, system, website):
        self.name = name
        self.lang = lang
        self.email = email
        self.system = system
        self.website = website

    def pythoner(self):
        pythoner_list = [ self.name, self.lang, self.email, self.system, self.website ]
        return pythoner_list
"""

class Programmer(Person):
    def __init__(self, name, lang, email, system, website):
        Person.__init__(self,name,lang,email)
        #self.name = name
        #self.lang = lang
        #self.email = email
        self.system = system
        self.website = website

    def pythoner(self):
        pythoner_list = [ self.name, self.lang, self.email, self.system, self.website ]
        return pythoner_list

if __name__=="__main__":
    writer = Person("qiwsir","Chinese","qiwsir@gmail.com")
    python = Programmer("qiwsir","Python","qiwsir@gmail.com","Ubutun","qiwsir.github.io")
    print "My name is:%s"%writer.author()
    print "I write program by:%s"%python.pythoner()[1]

