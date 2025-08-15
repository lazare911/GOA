def greet(L,num):
    res=[]
    for i in L:
        if i%num==0:
            res.append(i)
    return res
print(greet([1,23,165,2,3,92,10,34,911],3))