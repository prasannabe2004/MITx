class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

#w1 = Weird(X, Y)
#print w1.getX()
#w2 = Weird(X, Y)
#print w2.getY()

w1 = Wild(X, Y)
print w1.getX()
w2 = Wild(X, Y)
print w2.getY()

w3 = Wild(17, 18)
print w3.getX()
print w3.getY()

w4 = Wild(X, 18)
print w4.getX()
print w4.getY()

X = w4.getX() + w3.getX() + w2.getX()
#31
print X

#7
print w4.getX()

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
#44
print Y

#8
print w2.getY()



