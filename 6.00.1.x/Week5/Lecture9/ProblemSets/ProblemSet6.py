i = 0
n=10
while i < 5:
    #print 'hello'
    n *= 2
    i += 1

#print n

def iterPower(a, b):
   result = 1
   while b > 0:
       #print 'hello'
       result *= a
       b -= 1
   return result

#print iterPower(2,3)

def recurPower(a, b):
    #print a, b
    if b == 0:
        return 1
    else:
        return a * recurPower(a, b-1)
#print recurPower(3,10)

def recurPowerNew(a, b):
   print a, b
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)

recurPowerNew(4,50)
