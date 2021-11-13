
def my_mean(numbers):
    N = len(numbers)
    total = 0
    for num in numbers:
        total += num
    mean = total / N
    return mean
