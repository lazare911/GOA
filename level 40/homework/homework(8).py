def find_short(s):
    words = s.split()
    return len(min(words, key=len))