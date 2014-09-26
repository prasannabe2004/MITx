def myLog(x, b):
    y = 0
    c = 0
    while(x >= c):
        y = y + 1
        print c,y
        c = pow(b,y)
    return y-1

print myLog(16,2)
print myLog(15,3)