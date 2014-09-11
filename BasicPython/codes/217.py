#!/usr/bin/env python
#coding:utf-8

"""
class Person:
    def __init__(self, name, lang, website):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "qiwsir@gmail.com"
"""
class Person:
    def __init__(self, name, lang="golang", website="www.google.com"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "qiwsir@gmail.com"
    
    def author(self, address):
        #return self.name
        return laoqi.name+" in "+address

laoqi = Person("LaoQi")
info = Person("qiwsir",lang="python",website="qiwsir.github.io")

#print "laoqi.name=",laoqi.name
print "Author name from laoqi:",laoqi.author("China")
print "Author name from info:",info.author("Suzhou")
#print "info.name=",info.name
#print "-------"
#print "laoqi.lang=",laoqi.lang
#print "info.lang=",info.lang
#print "-------"
#print "laoqi.website=",laoqi.website
#print "info.website=",#info.website

