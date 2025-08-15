x = [1,2,3,3,4,5]
def sequence_mistake(element):
    for i in element:
        if i==3:
            element.pop(2)
    return element
print(sequence_mistake(x))