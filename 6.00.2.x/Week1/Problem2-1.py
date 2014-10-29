# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:49:31 2014

@author: pmohanasundaram
"""

def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e
    
#lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

#lotsOfParameters2(5,4,3,2,1)

def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

lotsOfParameters3(e=5,a=1,d=4,b=2,c=3)
