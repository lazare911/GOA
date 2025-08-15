def count_positives_sum_negatives(arr):
    z=[]
    l=[]
    L=[]
    n=[]
    S=[]
    for i in arr:
        if i<=-1:
            l.append(i)
        elif i>=1:
            L.append(i)
    if arr==[]:
        return []
    S.append(len(L))
    S.append(sum(l))
    return S
            