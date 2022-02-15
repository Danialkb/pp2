def reversed(s):
    c = []
    for i in range(len(s)-1, -1, -1):
        c.append(s[i])
    return c
print(*reversed(input().split()))