def sum(x,y):
    if type(x)==str or type(y)==str:
        return int(y)+int(x)
    elif type(x)==bool or type(y)==bool:
        return "ERROR"
    else:
        return x+y
print(sum(1,1.5))