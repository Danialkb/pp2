def unique(a):
    c = []
    for i in a:
        if i not in c:
            c.append(i)
    return c
print(*unique(list(map(int,input().split()))))