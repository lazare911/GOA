l=[1,2,2,3,3,4]
for i in l:
    if l.count(i)==2:
        l.remove(i)
print(l)