x=[1,-2,3,-4,5]
y=[-6,7,-8,9]
def calc_negative(L1,L2):
    P=[]
    N=[]
    for i in L1:
        if i>0:
            P.append(i)
        else:
            N.append(i)
    for i in L2:
        if i<0:
            N.append(i)
        else:
            P.append(i)
    return(sum(N),len(P))
print(calc_negative(x,y))