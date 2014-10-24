def sort3(lst):
    out = []
    k=0
    for iteration in range(0,len(lst)):
        k+=1
        print 'bye'
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            k+=1
            print 'hello'
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
        print L, iteration
    print k
    return out


#list = [90,80,70,60,50,40,30,20,10,0]
list = [0,10,20,30,40,50,60,70,90,100,200]

print sort3(list)