ar, a = [i for i in input().split()], []
for i in range(len(ar)):
    if len(ar[i]) >= 3:
        a.append(ar[i])
for i in range (len(a)):
    print(a[i], end=' ')