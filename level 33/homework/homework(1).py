def manual_split(text):
    space=" "
    result=[]
    current_word=""
    for i in text:
        if i==space:
            result.append(current_word)
            current_word=""
        else:
            current_word+=i
print(manual_split("hello world its me "))