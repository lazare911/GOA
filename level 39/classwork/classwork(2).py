def join_strings(char_list):
    result = ""
    i = 0
    while i < len(char_list):
        result += char_list[i]
        i += 1
    return result
letters = ['h','e','l','l','o']
print( join_strings(letters))