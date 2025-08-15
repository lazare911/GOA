def remove_smallest(numbers):
    a=numbers[:]
    for i in numbers:
        if i==min(a):
            a.remove(i)
            break
    return a