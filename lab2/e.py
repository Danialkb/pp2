n = list(map(int, input().split()))
x = None
if len(n) <= 1:
    x = int(input())
if x is None:
    x = n[1]
n = n[0]
a = [(x+2*i) for i in range(n)]
if n == 1:
    print(x)
    exit(0)
b = a[0]^a[1]
for i in range(2, n):
    b = b^a[i]
print(b)