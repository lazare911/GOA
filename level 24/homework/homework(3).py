def abbrev_name(name):
    n=[]
    s=[]
    y=name.split()
    n.append(y[0])
    s.append(y[1])
    n1=n[0]
    s1=s[0]
    x=n1[0]+"."+s1[0]
    return x.upper()
print(abbrev_name("Lazare Burduli"))
