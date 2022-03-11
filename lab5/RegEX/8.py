import re

a = input()

pattern = r'[A-Z][a-z]*[0-9]*'

print(re.findall(pattern, a))

# AbcAb47 -------- ['Abc', 'Ab47']