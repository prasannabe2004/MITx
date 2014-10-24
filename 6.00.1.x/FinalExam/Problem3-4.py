k = 0
def sort4(lst):
    global k
    k += 1
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions assume this line just executed
        print L
        print k
        return unite(front, back)


list = [90,80,70,60,50,40,30,20,10,0]
#list = [0,10,20,30,40,50,60,70,90,100]

print sort4(list)