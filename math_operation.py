import math


def get_operation(temp: list):
    if len(temp) == 1:
        result = math.__dict__[temp[0]]
    elif temp[0] == 'abs':
        result = abs(*[float(i) for i in temp[1:]])
    elif temp[0] == 'round':
        result = round(*[float(i) for i in temp[1:]])
    else:
        result = math.__dict__[temp[0]](*[float(i) for i in temp[1:]])
    return result
