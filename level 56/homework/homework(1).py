x='banana'
res=''
l=[]
for i in x:
    l.append(x.count(i))
    if x.count(i)==max(l):
        res=i
print(res)