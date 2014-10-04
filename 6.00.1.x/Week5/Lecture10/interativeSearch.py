def search(list, element):
    for e in list:
        if e == element: 
            return True
    return False

L = [5, 0, 2, 4, 6, 3, 1]

print search(L,8)