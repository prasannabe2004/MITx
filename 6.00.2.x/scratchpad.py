# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:27:46 2014

@author: pmohanasundaram
"""

import random

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 


def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)

      
for i in range(10):
    #print 'dist1 ', dist1()
    #print 'dist2 ', dist2()
    #print 'dist3 ', dist3()
    #print 'dist4 ', dist4()
    #print dist5()
    print dist6()