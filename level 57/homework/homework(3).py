def is_even(num):
    l1=[]
    l2=[]
    for i in num:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    return (f'this {l1} is even',f'this {l2} is odd ')
print(is_even([1,2,3,4,5,6,7,8]))