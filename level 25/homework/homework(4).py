def twice_as_old(dad_years_old, son_years_old):
    x=dad_years_old-(son_years_old*2)
    if x<0:
        return -x
    else:
        return x
print(twice_as_old(65,21))