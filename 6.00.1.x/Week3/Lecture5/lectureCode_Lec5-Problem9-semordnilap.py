def semordnilap(str1,str2):
    print str1,str2,len(str1),len(str2)
    if len(str1) < 1 or  len(str2) < 1:
        if str1 == str2:
            return True
        else:
            return False
    else:
        return semordnilap(str1[1:len(str1)],str2[0:-1])
    

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
    
    return semordnilap(str1, str2)


print semordnilapWrapper("abc","cba")