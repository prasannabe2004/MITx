def isWordGuessed(secretWord, lettersGuessed):
    k = len(secretWord)
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j] and k>=1:
                k = k - 1
    if k == 0:
        return True
    return False

print isWordGuessed('apple',['e', 'o', 'u', 'p', 'l', 's'])
print isWordGuessed('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't'])

def isWordGuessesNew(secretWord, lettersGuessed):
    return set(secretWord) <= set(lettersGuessed)

print isWordGuessesNew('apple',['e', 'o', 'u', 'p', 'l', 's'])
print isWordGuessesNew('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't'])

def getGuessedWord(secretWord, lettersGuessed):
    temp = ['' for i in range(len(secretWord))]
    string = ""
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                temp[j] = secretWord[j]
    print "temp ", str(temp)
    for i in range(len(temp)):
        if temp[i] != '':
            string = string+temp[i]
        else:
            string = string+ '_ '
    print string
    return string

print getGuessedWord('apple',['e', 'o', 'a', 'z', 'l', 's'])
print getGuessedWord('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't'])


def getAvailableLetters(lettersGuessed):
    alphaset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        if i in alphaset:
            alphaset.remove(i)
    str1 = ''.join(alphaset)
    return str1

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
print getAvailableLetters(['i', 'v', 'm', 's', 'd', 'b'])
print getAvailableLetters(['q', 'w', 'n', 'l', 'z', 'h', 'u', 'r', 'a', 'm', 'b'])
