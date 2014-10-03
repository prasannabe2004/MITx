def lenRecur(s):
    print 'kello'
    if s == '':
        return 0
    else:
        return 1 + lenRecur(s[1:])

#print lenRecur('pra')

def isIn(a, s):
    '''
    a is a character, or, singleton string.
    s is a string, sorted in alphabetical order.
    '''
    print 'hello'
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return a == s
    else:
        test = s[len(s)/2]
    if test == a:
        return True
    elif a < test:
        return isIn(a, s[:len(s)/2])
    else:
        return isIn(a, s[len(s)/2+1:])

#print isIn('a','abcdefghijklmnopqrstuvwxyz')


def union(L1, L2):
    '''
    L1 & L2 are lists of the same length, n
    '''
    i = 0
    j = 0
    temp = L1[:]
    for e2 in L2:
        i+=1
        #print 'hai'
        flag = False
        for check in temp:
            #print 'hello'
            j+=1
            if e2 == check:
                flag = True
                break
        if not flag:
            temp.append(e2)
    print i,j
    return temp

#print union([1,2,3,4,5,6],[11,12,13,14,15,16])

def unionNew(L1, L2):
    '''
    L1 & L2 are lists of the same length, n
    '''
    i=0
    j=0
    temp = []
    for e1 in L1:
        i+=1
        #print 'hello'
        flag = False
        for e2 in L2:
            j+=1
            #print 'hai'
            if e1 == e2:
                flag = True
                break
        if not flag:
            temp.append(e1)
    print i,j
    return temp + L2

print unionNew([1,2,3,4,5,6],[11,12,13,14,15,16])