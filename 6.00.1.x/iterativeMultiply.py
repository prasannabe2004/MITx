def iterativeMultiply(a,b):
    result = 0
    for i in range(b):
        result = result + a
    return result


result = iterativeMultiply(50,6)
print "a times b is: " , str(result)