def my_function(numbers):
    l=[]
    g=0
    for g in range(0,len(numbers)):
        l.append(numbers[g])
        g+=1
    return sum(l)
my_list = [3, 5, 7, 2, 8]
print(my_function(my_list))