def lenIter(aStr):
    i = 0
    if aStr == '':
        return 0
    while aStr[0:i] != aStr[0:-1]:
        i = i+1
    return i+1

print lenIter("hello")