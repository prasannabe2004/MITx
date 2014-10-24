def sort1(lst):
    swapFlag = True
    iteration = 0
    k = 0
    while swapFlag:
        k+=1
        swapFlag = False
        for i in range(len(lst)-1):
            k+=1
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        iteration += 1
    print k
    return lst

list = [90,80,70,60,50,40,30,20,10,0]

print sort1(list)
