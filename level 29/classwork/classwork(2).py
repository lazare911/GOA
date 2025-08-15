def rep(inp):
    x =[]
    for i in inp:
        if i == 97:
            x.append("a")
        elif i==101:
            x.append("e")
        elif i== 105:
            x.append("i")
        elif i==111:
            x.append("o")
        elif i== 117:
            x.append("u")
        else:
            x.append(i)
        return x
        