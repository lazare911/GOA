def sum_list(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total
my_list = [3, 5, 7, 2, 8]
print("sum:", sum_list(my_list))