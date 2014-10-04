def rSearch(list,element):
    if element == list[0]:
        return True
    if len(list) == 1:
        return False
    return rSearch(list[1:],element)


L = [5, 0, 2, 4, 6, 3, 1]

print rSearch(L,6)