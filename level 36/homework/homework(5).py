def accum(st):  
    str=""
    x=0
    for i in st:
            str+=i.upper()+i.lower()*x+'-'
            x+=1
    a=str[:-1]
    return a