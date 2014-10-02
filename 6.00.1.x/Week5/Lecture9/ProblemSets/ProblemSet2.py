#1+3*1000+5*n +1+1
def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total


#1+2*1000+5*(log2(n)) +2
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x /= 2
        total += x

    return total

#1+1+3*n+4*n-1+1
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x
    i = 0
    for x in L:
        i= i +1
        if highestFound == None:
            i= i +1
            print '1+2'
            highestFound = x
            i= i +1
        elif x > highestFound:
            i= i +2
            print '1+3'
            highestFound = x
            i= i +1
    print 'i=',i
    return (totalSum, highestFound)


print program3([1,2,3,4,5,6,7,8,9,10])