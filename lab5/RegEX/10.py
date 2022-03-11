import re

name = input()

pattern = r'(?<!^)(?=[A-Z])'
name = re.sub(pattern, '_', name).lower()
print(name)