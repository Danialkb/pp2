a, b = list(map(int, input().split())), 0
for i in range(len(a)):
    posi = b+a[b]+1
    for j in range(b, posi):
        print(b+a[b], a[j] + j)
        if b + a[b] < a[j] + j:
            b = j
        elif posi >= len(a):
            print(1)
            exit(0)
print(0)