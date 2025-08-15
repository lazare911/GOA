L = [1,3,5,7]
l = 0
def manual_append(x,y):
    x.insert(len(x),y)
    return x
print(manual_append(L,l))    