x= int(input("enter number:"))
def greet(num):
    if num%2==0:
        num+=5
        return num%5
    else:
        num=num*3
        return num%5
           
print(greet(x))