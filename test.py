import operator

OPERATORS = ['+', '/', '*', '-', '(', ')', '^']

input_string = 'sin(pi/2^1) + log(1*4+2^2+1.3^2)'

temp = ''
expression = []
for i in input_string:
    if i not in OPERATORS:
        temp += i
    else:
        expression.append(temp)
        expression.append(i)
        temp = ''
if temp:
    expression.append(temp)

while ' ' in expression:
    expression.remove(' ')

print(expression)

expression_2 = []
for i in expression:
    if i.isalpha():
