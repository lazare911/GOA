def sum_array(a):
    for i in a:
        if type(i)==int or type(i)==float:
            return sum(a)
        else:
            return 0
    if a==[]:
        return 0
print(sum_array([1,2,3,4,5,6]))