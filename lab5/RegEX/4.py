import re

a = input()

pattern = r'(?P<naiti>[A-Z][a-z]+)'

print(re.findall(pattern, a))
# print(re.search(pattern, a).group('naiti')) if re.search(pattern, a) != None else print('Ne naideno')

#akakAkk -------- ['Akk']
#a888Alsoa; ------ ['Alsoa']
# AgKdIe ---- ['Ag', 'Kd', 'Ie']
