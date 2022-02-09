b = int(input())
a = [[0 for i in range(b)] for j in range(b)]
for i in range(b):
    for j in range(b):
        if i == j:
            a[i][j] = i*j
        elif i == 0:
            a[i][j] = j
        elif j == 0:
            a[i][j] = i
for i in range(b):
    for j in range(b):
        print(a[i][j], end=' ')
    print()