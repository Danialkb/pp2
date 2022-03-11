def squares(a, b):
    for i in range(a, b):
        yield i**2

for i in squares(int(input()), int(input())+1):
    print(i, end=' ')
