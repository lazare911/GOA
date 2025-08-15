def greet(x,y):
    if type(x)==bool or type(y)==bool:
        return "Error"
    if y==0:
        return "ZeroDivissionError"
    if x>y:
        return x/y
    elif y>x:
        return y/x
    
print(greet(10,25))