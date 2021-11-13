
from .averages import my_mean

def my_cov(list_x, list_y):
    assert len(list_x) == len(list_y)
    N = len(list_x)
    xbar = my_mean(list_x)
    ybar = my_mean(list_y)
    total = 0
    for i in range(len(list_x)):
        total += ((list_x[i] - xbar) * (list_y[i] - ybar))
    return total / N

def my_var(list_x):
    return my_cov(list_x, list_x)
