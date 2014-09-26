animals = {'A': [11, 19, 8, 2], 'B': [], 'f': [5], 'M': [0, 7, 20], 'n': [5], 'P': [9, 3, 6, 17], 'U': [9, 4], 'Y': [18, 13, 7, 20, 14]}
def howMany(aDict):
    k = 0
    if len(aDict) == 0:
        return None
    local=[]
    for key, value in aDict.iteritems():
        if k<=len(value):
            k = len(value)
            local = key
    return str(local)

print howMany(animals)