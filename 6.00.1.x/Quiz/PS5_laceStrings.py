def laceStrings(s1, s2):
    s1len = len(s1)
    s2len = len(s2)
    s3 = ""

    if s1len > s2len:
        s4 = s1[s2len:]
        length = s2len
    else:
        s4 = s2[s1len:]
        length = s1len

    for i in range(length):
        s3 = s3 + s1[i]
        s3 = s3 + s2[i]

    return s3+s4

print laceStrings("abcdefghijklmnopqr", "0123456789")