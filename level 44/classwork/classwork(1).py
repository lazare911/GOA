def sum_mul(n, m):
    total = 0
    if  m<=0 or n<=0:
        return "INVALID"
    elif n==m:
        return 0
    elif m>0 and n>0:
        for i in range(n, m, n):
            total+=i
    return total