l=[1,2,3,4,5,6,7,8]
l1=[]
g=l.sort()
for i in g:
    if i%2==0:
        l1.append(i)
for i in g:
    if i%2==1:
        l1.append(i)
print(l1)
