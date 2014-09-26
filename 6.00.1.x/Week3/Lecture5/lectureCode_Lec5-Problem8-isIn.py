

def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if(char == aStr):
            return True
        
    mid = len(aStr)/2
    midchar = aStr[mid]
    

    if mid == 0:
        return False
    if midchar == char:
        return True
    elif midchar > char:
        return isIn(char,aStr[:mid])
    elif midchar < char:
        return isIn(char,aStr[mid:])
        
print isIn('e',"e")