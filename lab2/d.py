b = int(input())
a = [['.' for i in range(b)] for j in range(b)]
if b % 2 == 1:
    for i in range(b):
        for j in range(b):
            if i+j+1 >= b:
                a[i][j] = '#'
else:
    for i in range(b):
        for j in range(b):
            if j - i <= 0:
                a[i][j] = '#'
for i in range(b):
    for j in range(b):
        print(a[i][j], end='')
    print()