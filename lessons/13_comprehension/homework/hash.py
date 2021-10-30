
from functools import reduce

def get_name_hash(name):
    name_lower = map(lambda x: x.lower(), name)
    ascii_name = map(ord, name_lower)
    
    ascii_letters = list(filter(lambda x: x != 32, ascii_name))
    N = len(ascii_letters)

    ascii_mean = reduce(lambda x, y: x + y, ascii_letters) / N
    squared_devs = map((lambda x: (x - ascii_mean)**2), ascii_letters)
    name_hash = reduce(lambda x, y: x + y, squared_devs) / N
    return name_hash
