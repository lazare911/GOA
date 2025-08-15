def check_vowel(strng, position):
    if position+1>len(strng):
        return False
    elif position<0:
        return False
    elif strng[position]=='a' or  strng[position]=='e' or  strng[position]=='i' or  strng[position]=='o' or  strng[position]=='u' or strng[position]=='A' or  strng[position]=='E' or  strng[position]=='I' or  strng[position]=='O' or  strng[position]=='U':
        return True
    else:
        return False