def generate_pairs(n):
    r= []
    for i in range (0,n+1):
        for j in range (i,n+1):
            r.append([i,j])
    return r