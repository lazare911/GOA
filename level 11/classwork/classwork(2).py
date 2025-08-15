
def solution(string):
    x = ''
    for i in string:
        x = i + x
    return x
print(solution('hello'))