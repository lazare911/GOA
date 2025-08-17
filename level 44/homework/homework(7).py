def square_digits(num):
    g=""
    x=str(num)
    for i in x:
        s=int(i)*int(i)
        g+=str(s)
    return int(g)
        