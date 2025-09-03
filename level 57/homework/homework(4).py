
students = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76,
}
students.update({'nino':100,})
for i , p in students.items():
    if p > 90:
        print(i)

