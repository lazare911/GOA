l=[1,2,2,3,3,4,5,6,6,7]
l1=[]
for i in l:
    if l.count(i)>=2:
        l1.append(i)
print(l1)