def recurPowerNew(base,exp):
    if exp == 0:
        return 1
    elif exp%2 == 0:
        return recurPowerNew(base*base,exp/2)
    else:
        return base*recurPowerNew(base,exp-1)

result = recurPowerNew(2.0,16)
print "a to the power of b is: " , str(result)