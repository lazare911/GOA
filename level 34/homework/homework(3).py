def dont_give_me_five(start,end):
    l1=[]
    l2=[]
    for i in range(start,end+1):
        if "5" in str(i) :
            l1.append(int(i))
        else:
            l2.append(int(i))
    return len(l2)
