def histogram(a):
    for i in range(len(a)):
        a[i] = '*'*a[i]
    return a
print(*histogram(list(map(int, input().split()))),sep='\n')