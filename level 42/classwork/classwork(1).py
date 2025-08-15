def unique_sum(lst):
    x=0
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            continue
        else:
            x+=lst[i]
    if lst==[]:
        return None
    else:
        return x