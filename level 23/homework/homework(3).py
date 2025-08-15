def strings(x,y):
    if type(x)==int or type(y)==str:
        return str(y)+str(x)
    elif type(y)==int and type(x)==str:
        return str(x)+str(y)
print(strings("h",1))