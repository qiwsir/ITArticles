#!/usr/bin/env python
#coding:utf-8

import random

numbers = [random.randint(1,100) for i in range(20)]

"""
odd = []
even = []

for x in numbers:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
"""

odd = [x for x in numbers if x%2!=0]
even = [x for x in numbers if x%2==0]

print numbers
print "odd:",odd
print "even:",even
