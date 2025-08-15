L=[1,2,3,4,5,6,7,8]
number=7

def manual_index(x,y):
    for i in range(1,len(L)) :
        if x[i]==y:
            return i
print(manual_index(L,number))

