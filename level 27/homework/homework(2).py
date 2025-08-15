y=input("Enter password: ")
def password(x):
    if len(x)<8:
        return "try again your password must have 8 characters"
    return "password accepted"
print(password(y))