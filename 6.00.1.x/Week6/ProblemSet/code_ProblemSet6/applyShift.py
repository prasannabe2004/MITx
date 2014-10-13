import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO
    dict={}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for i in range(len(upper)):
        dict[upper[i]] = upper[(i+shift)%26]
    for j in range(len(lower)):
        dict[lower[j]] = lower[(j+shift)%26]
    return dict

print buildCoder(3)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO

    mystr = ''
    for i in text:
        if i in string.uppercase:
            mystr= mystr + coder[i]
        elif i in string.lowercase:
            mystr = mystr + coder[i]
        else:
            mystr = mystr + i
    return mystr


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))


print applyShift('This is a test.', 8)


