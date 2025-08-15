#              INPUT
def num(x):
    y=0
    for i in range(len(x)):
        y+=x[i]
    return y

#             OUTPUT
print(num([1,2,3,4,5,6,7,8,9,15]))