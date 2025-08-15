def count_positives_sum_negatives(arr):
    l=[]
    s=[]
    G=[]
    n=''
    for i in arr:
        if i > 0:
            l.append(i)
        elif i < 0:
            s.append(i)
        else:
            G.append(i)
    G=[len(l),sum(s)]        
    return G
   