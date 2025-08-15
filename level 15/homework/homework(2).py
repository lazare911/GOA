L = [1,2,3,4,5,6]
y = int(input("choose index u want to change:"))
x = input("input anything u want:")
def add_element(index,element):
    L.insert(index,element)
    return L
print(add_element(y,x)) 
