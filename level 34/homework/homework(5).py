def remove_smallest(numbers):
    for i in numbers:
        if i==min(numbers):
            numbers.remove(i)
            break
    return numbers