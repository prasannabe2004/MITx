def gcdIter(a,b):
    if a<b:
        gcd = a
    else:
        gcd = b
    while gcd >= 1:
        if a%gcd == 0 and b%gcd == 0 :
            break
        gcd = gcd - 1    
    return gcd

result = gcdIter(17,12)
print "GCD of a and b is: " , str(result)