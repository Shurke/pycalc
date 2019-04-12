import operator
import re
import math

OPERATORS = {'+': (1, operator.add), '-': (1, operator.sub),
             '*': (2, operator.mul), '/': (2, operator.truediv),
             '//': (2, operator.floordiv), '%': (2, operator.mod),
             '^': (3, operator.pow)}


def parse(expression_string):
    temp = ''
    expression_parsed = []
    for i in expression_string:
        if i.isalpha():
            temp += i
        if i.isdigit() or i == '.':
            temp += i
        elif temp:
            if temp.isalpha():
                expression_parsed.append(temp)
            else:
                expression_parsed.append(float(temp))
            temp = ''
        if i in OPERATORS or i in '()':
            expression_parsed.append(i)
    if temp:
        expression_parsed.append(float(temp))
    return expression_parsed


input_string = 'sin(pi/2^1) + log(1*4+2^2+1.3^2)'

print(parse(input_string))
