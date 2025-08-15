def index(n):
    if type(n)==str:
        return "Literature"
    elif type(n)==bool:
        return  "Math"
    elif type(n)==int or type(n)==float:
        return "Science"