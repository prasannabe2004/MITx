x = [2,1]
y = [2,1]
z = False
if x == y:
    if sorted(x) == sorted(y):
        print 'hello'
        if x.sort() == y.sort():
            z =  x.sort() == sorted(y)
print z

