num= int(input("enter number:"))
def greet(num):
    x=0
    for i in str(num):
        x+=int(i)
    return int(num)%x 
print(greet(num))