#1+3*n*n+n+1
def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

print program1([1,2,3,4,5])


def program2(L):
    i = 0
    squares = []
    i = i+1
    for x in L:
        i = 1+1
        for y in L:
            i =i +1
            if x == y:
                squares.append(x*y)
                i=i+3
    i =i +1
    print 'i =',i
    return squares

print program2([1,2,3,4,5])

def program3(L1, L2):
    i =0
    intersection = []
    for elt in L1:
        i = i +1
        if elt in L2:
            i = i +1
            intersection.append(elt)
    print 'i=',i
    return intersection

print program3([1,2,3,4,5],[10,20,30,40,50])