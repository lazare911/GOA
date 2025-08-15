x=[1,2,3,4,5]
y=[6,7,8,9,10]
def sum_comparison(L,l):
    if sum(L)>sum(l):
        return L
    return l
print(sum_comparison(x,y))