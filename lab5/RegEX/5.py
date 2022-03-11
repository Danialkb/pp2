import re

a = input()

pattern = r'.*(?P<naiti>a+.*b$)'

print('Nice!') if re.search(pattern, a) != None else print('FAIL')
