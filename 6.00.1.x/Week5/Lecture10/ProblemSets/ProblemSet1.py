a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

def foo(L):
    val = L[0]
    while (True):
        val = L[val]

#foo(a)
#foo(b)
#foo(c)


num = 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

#print val

num = 9
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val
