def digitize(n):
    l=[]
    for i in str(n):
        l.append(int(i))
    return l[::-1]
print(digitize(16585418))