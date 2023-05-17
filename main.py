import re
pattern = '\d+'
string = 'hello 12 hi 89 howdy 3422'
output = re.split(pattern, string)
print(output)