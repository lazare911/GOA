def is_opposite(s1,s2):
    if s1 == "" or s2  == "":
        return False
    for chr in range(0,len(s1)) :
        if  s1[chr] == s2[chr]:
            return False
    else:
        return True