# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def is_palindrome(s):
    x=s.lower()
    if x == x[::-1]:
        return True
    else:
        return False
