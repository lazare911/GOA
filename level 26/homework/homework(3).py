def change_list(l):
    f=[]
    b=[]
    s=[]
    i=[]
    for x in l:
        if type(x)==float:
            f.append(x)
        elif type(x)==bool:
            b.append(x)
        elif type(x)==str:
            s.append(x)
        elif type(x)==int:
            i.append(x)
    if len(l)-1==len(f) and type(l[-1])==int:
        l.append(float(l[-1]))
        l.pop(-2)
    if len(l)-1==len(f) and type(l[-1])==str:
        l.pop(-1)
    if len(l)-1==len(f) and type(l[-1])==bool:
        l.pop(-1)
    if len(l)-1==len(b) and type(l[-1])==int:
        l.pop(-1)
    if len(l)-1==len(b) and type(l[-1])==str:
        l.pop(-1)
    if len(l)-1==len(b) and type(l[-1])==float:
        l.pop(-1)
    if len(l)-1==len(s) and type(l[-1])==int:    
        l.append(str(l[-1]))
        l.pop(-2)
    if len(l)-1==len(s) and type(l[-1])==float:
        l.append(str(l[-1]))
        l.pop(-2)
    if len(l)-1==len(s) and type(l[-1])==bool:
        l.append(str(l[-1]))
        l.pop(-2)
    if len(l)-1==len(i) and type(l[-1])==float:
        l.append(int(l[-1]))
        l.pop(-2)
    if len(l)-1==len(i) and type(l[-1])==str:
        l.pop(-1)
    if len(l)-1==len(i) and type(l[-1])==bool:
        l.pop(-1)
    return l
#______________________________________________

print(change_list([1,2,3,4,12.5]))
print(change_list(['1','2','3',123]))
print(change_list([True,False,True,"___"]))
print(change_list([1.1,2.2,3.3,12]))
