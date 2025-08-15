def filter_list(l):
    s=[]
    for i in l:
        if type(i)==int:
            s.append(i)
    return s
