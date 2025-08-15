G =[1,2,3,4,6]
def manual_sum(L):
    res = 0
    if type(L) == list:
        for i in L:
            res+=i
        return res
print(manual_sum(G))
