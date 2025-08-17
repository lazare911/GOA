def get_middle(s):
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    else:
        return s[mid-1:mid+1]
