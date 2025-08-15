def greet(n):
    x=0
    y=[]
    for i in n:
        if i%2==0:
            x+=i
        if i%2==1:
            y.append(n)
                
    return [len(y),x] 
print(greet([1,4,3,6,9,11,17,13,26,30]))