def accum(st):  
    str=""
    x=0
    for i in st:
        if i!=st[-1]:
            str+=i.upper()+i.lower()*x+"-"
            x+=1
        else:
            str+=i.upper()+i.lower()*x
    return str
print(accum('hello'))