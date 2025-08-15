def most_data_types(l):
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
    if len(f)>len(b) and len(f)>len(i) and len(f)>len(s):
        return "most basic data type in this list is float"    
    if len(b)>len(f) and len(b)>len(i) and len(b)>len(s):
        return "most basic data type in this list is boolean"    
    if len(s)>len(b) and len(s)>len(i) and len(s)>len(f):
        return "most basic data type in this list is string"
    if len(i)>len(b) and len(i)>len(f) and len(i)>len(s):
        return "most basic data type in this list is integer"
#___________________________________________________________

print(most_data_types([1,2,"3","4","5","6","7",1.0,1.1,1.2,True,False]))