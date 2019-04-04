import re

s = 'pow(2, 3)'
pattern = r"([a-z]+[0-9]"
print(re.split(pattern, s))
