D=int(input("Enter day: "))
M=int(input("Enter month: "))
Y=int(input("Enter year: "))
def day_month_year(day,month,year):
    return f"{day}/{month}/{year}"
print(day_month_year(D,M,Y))