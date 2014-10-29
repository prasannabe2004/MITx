# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 17:14:49 2014

@author: pmohanasundaram
"""

import pylab

def loadFile():
    inFile = open('julyTemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)


def plotGraph(low,high):
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    diff = []
    for i in range(0,31):
        diff.append(high[i] - low[i])
    pylab.plot(range(1,32),diff)
    pylab.show()


low, high = loadFile()
plotGraph(low,high)