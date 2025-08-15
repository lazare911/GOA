def even_last(numbers):
    res=0
    if len(numbers)==0:
        return 0
    for i in range(0,len(numbers),2):
        res+=numbers[i]  
    return res*numbers[-1]
print(even_last([1,2,3,4,7,3,98,36]))