def calc(x):
    total1, t1, t2 = "", 0, 0
    for i in x:
        total1 += str(ord(i))
    for j in total1:
        t1 += int(j)
        if j == "7": t2 += 1
        else: t2 += int(j)
    return max(t1,t2) - min(t1,t2)