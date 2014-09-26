animals = {'A': [11, 19, 8, 2], 'B': [], 'f': [5], 'M': [0, 7, 20], 'n': [5], 'P': [9, 3, 6, 17], 'U': [9, 4], 'Y': [18, 13, 7, 20, 14]}
def howMany(aDict):
    k=0
    for i in aDict.values():
        for j in i:
            #print j
            if j != None:
                k = k+1
    return k

print howMany(animals)