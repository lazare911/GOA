def positive_sum(arr):
    x=0
    for i in arr:
        if i>0:
            x+=i
        else:
            i==0
    return x
print(positive_sum([-1,2,4,6,-7]))