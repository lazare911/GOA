def reverse_words(s):
    y=""
    g=s.split()
    x=g[::-1]
    for i in x:
        y+=i+" "
    return y.strip()