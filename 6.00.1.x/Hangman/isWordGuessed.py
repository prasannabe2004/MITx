def isWordGuessed(secretWord, lettersGuessed):
    k = len(secretWord)
    print "k= ", k
    for i in lettersGuessed:
        for j in secretWord:

            if i == j:
                print i,j
                k = k -1;
                if k == 0:
                    return True
            if k == 0:
                return True
    return False
print isWordGuessed('apple',['e', 'o', 'a', 'p', 'l', 's'])
print isWordGuessed('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't'])