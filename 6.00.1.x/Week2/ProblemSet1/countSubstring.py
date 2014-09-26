def countSubstring(str1):
    count = 0
    next = 0
    got = 0
    for i in range(len(str1)):
        next = str1.find("bob",count)
        if(next != -1):
            count = next+1
            got = got +1
        else:
            break
    return got

s = 'opsoobbobbbobbknbobobkbobbmoebobbk'
got = countSubstring(s)
print "Number of times bob occurs is: " , str(got)