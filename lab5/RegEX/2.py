import re
a = input()

pattern = r'a+b{2,3}'

if re.search(pattern, a) == None:
    print('FAIL')
else:
    print('IT IS OK')