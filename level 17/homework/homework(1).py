L=[1,2,3,4,5,6,7]
number=4
def manual_remove(x,y):
    for i in x:
        if i==y:
            x.pop(i)
            return x
print(manual_remove(L,number))