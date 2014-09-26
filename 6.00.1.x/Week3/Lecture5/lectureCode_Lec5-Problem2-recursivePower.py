def recursivePower(base,exp):
    if exp == 0:
        return 1
    else:
        return base*recursivePower(base,exp-1)

result = recursivePower(3.0,0)
print "a to the power of b is: " , str(result)