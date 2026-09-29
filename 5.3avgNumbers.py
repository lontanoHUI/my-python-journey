def avg(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


print(avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
