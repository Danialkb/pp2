a = list(map(int,input().split()))
posi = len(a) - 1
for i in range(len(a) - 2, -1, -1):
    if i + a[i] >= posi:
        posi = i
print(1) if posi == 0 else print(0)