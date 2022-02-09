q, n, q1 = [], int(input()), []
for i in range(n):
    a = list(input().split())
    x = int(a[0])
    if len(a) == 1:
        q1.append(q[0])
        q.pop(0)
    if x == 1:
        q.append(a[1])
print(*q1)