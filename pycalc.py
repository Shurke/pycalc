import re

import math_operation
import calculator

input_string = input('Enter your expression: ')




"""
temp = list()
s = str()
for i in test_string:
    if i not in ['(', ',', ')']:
        s += i
    else:
        temp.append(s)
        s = str()
temp.append(s)
if '' in temp:
    temp.remove('')
"""

print(calculator.eval_(input_string))
#print(math_operation.get_operation(temp))
