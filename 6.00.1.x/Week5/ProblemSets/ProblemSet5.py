def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result

#print multlist(3,[1,2,3,4,5,6])

def foo(n):
    print 'hai'
    if n <= 1:
        return 1
    return foo(n/2) + 1

#print foo(1)

def recur(n):
    global i
    i += 1
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)

#print recur(30),i

def baz(n):
    k = 0
    for i in range(n):
        for j in range(n):
            k+=1
            print i,j
    print k

print baz(40)