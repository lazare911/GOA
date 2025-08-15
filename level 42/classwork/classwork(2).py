def doubles(s):
    x = []
    for i in s:
        if x and x[-1] == i:
            x.pop()  
        else:
            x.append(i)
    return ''.join(x)