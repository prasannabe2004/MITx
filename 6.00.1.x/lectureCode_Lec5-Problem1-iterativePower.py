def iterativePower(a,b):
    result = 1.0
    for i in range(b):
        result = result * a
    return result

result = iterativePower(3.2,3)
print "a to the power of b is: " , str(result)