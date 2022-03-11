import re
a = input()

pattern = r'.*[a]+[b]*'

if re.search(pattern, a) == None:
    print('FAIL')
else:
    print('IT IS OK')