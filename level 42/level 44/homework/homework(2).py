def find(n):
    x=0
    for i in range(n+1):
        if i%3==0 or i%5==0:
            x+=i
    return x