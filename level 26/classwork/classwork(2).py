def multiply(n):
    z=len(str(n))
    s=len(str(n))-1
    if n<0:
        return n*5**int(s)
    else:
        return n*5**int(z)
print(multiply(50))