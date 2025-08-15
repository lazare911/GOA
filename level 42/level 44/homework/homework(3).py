def get_middle(s):
    n = len(s)
    middle = n // 2
    if n%2==0:
        return s[middle]
    else:
        return s[middle-1:middle+1]
    