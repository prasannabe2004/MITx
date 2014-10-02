def linearSearch(L, x):
    i=0
    for e in L:
        i= i+2
        if e == x:
            i=i+1
            print 'true i=',i
            return True
    i=i+1
    print 'false i=',i
    return False

linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12, 89], 26)