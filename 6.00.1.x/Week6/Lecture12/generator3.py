def genOneMillion():
    maxNum = 1000000
    current = -1
    while current < maxNum:
        current += 1
        yield current

test = genOneMillion()


print test.next()
print test.next()