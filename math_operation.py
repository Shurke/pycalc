import math

constants = ['e', 'inf', 'nan', 'pi', 'tau']


def get_operation(temp: list):
    if temp[0] in constants:
        result = math.__dict__[temp[0]]
    else:
        result = math.__dict__[temp[0]](*[float(i) for i in temp[1:]])
    return result
