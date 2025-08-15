def sum_list(word):
    l=""
    g=0
    for g in range(0,len(word)):
        l+=word[g]
        g+=1
    return l
letters = ['h','e','l','l','o']
print(sum_list(letters))