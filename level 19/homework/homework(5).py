x=[1,2,3,4,5,6,7]
def double_num(L):
    for i in L:
        L.append(i+i)
    return L
print(double_num(x))