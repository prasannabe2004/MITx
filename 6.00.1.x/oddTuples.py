def oddTuples(atuple):
    """
    This function return a new tuple with odd numbers
    :rtype : a tuple with even positions (i.e) odd elements
    """
    print len(atuple)
    got = ()
    print type(got)
    for i in range(0, len(atuple), 2):
        got = got+(atuple[i],)
    return got

input_tuple = ('I', 'am', 'a', 'test', 'tuple')
output = oddTuples(input_tuple)
print "New tuple is: ", output
