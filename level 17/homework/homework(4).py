L=[1,2,3,4,5,6]
index=2
def manual_pop(x,y):
    for i in x:
        if i==x[y]:
            x.remove(i)
    return x        
print(manual_pop(L,index))