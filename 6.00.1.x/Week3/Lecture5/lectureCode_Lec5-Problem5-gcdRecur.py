def gcdRecur(a,b):
    if b == 0:
        return a
    else:    
        return gcdRecur(b,a%b)

result = gcdRecur(9,12)
print "GCD of a and b is: " , str(result)