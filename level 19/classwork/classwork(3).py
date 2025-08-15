L=[1,2,3,4,5,6,7,8,9]
def GG(y):
    res=[]
    for i in y:
        if i%2==0:
            res.append(i)
    return res
print(GG(L))

