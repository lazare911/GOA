def descending_order(num):
    s=''
    n=str(num)
    g=" ".join(n)
    x=g.split()
    x.sort()
    for i in x[::-1]:
        s+=i
    return int(s)
    
        
        