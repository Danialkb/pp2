import re

a = input()

pattern = r'.*a+.*b$'

print('Nice!') if re.search(pattern, a) != None else print('FAIL')
# fksfjsdfjadfhjsdfhuufeb  --- Nice!