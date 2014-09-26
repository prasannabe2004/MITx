def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    x = 0
    k = start
    while(k<stop):
        x = x+ step * f(k)
        k = k+step
    return x


print radiationExposure(0, 5, 1)
