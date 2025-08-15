x=[1,2,3,4,5,6,7,8,9]
def delete_num(L):
    for i in L:
        if i%3==0:
            L.remove(i)
    return L
print(delete_num(x))