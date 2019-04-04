import math_operation


test_string = 'abs(-5)'

temp = list()
s = str()

for i in test_string:
    if i not in ['(', ',', ')']:
        s += i
    else:
        temp.append(s)
        s = str()
temp.append(s)
if '' in temp: temp.remove('')

print(math_operation.get_operation(temp))
