a, c = input(), True
b = a.split()
for i in range(2, int(b[0])):
    if int(b[0]) % i == 0:
        c = False
        break
if int(b[1]) % 2 == 1 or int(b[0]) > 500 or c == False:
    print('Try next time!')
else:
    print('Good job!')