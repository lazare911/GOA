x=input("Enter 3 numbers: ")
def max_number(y):
    l=[]
    res=y.split()
    for i in res:
        l.append(int(i))
    return max(l)
print(max_number(x))

