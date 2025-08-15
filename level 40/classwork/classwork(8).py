def high_and_low(numbers):
    l=numbers.split()
    x=[]
    for i in l:
        x.append(int(i))
    return str(max(x))+" "+str(min(x))