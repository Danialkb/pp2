a, b, j = input(), 0, 0
for i in range(len(a)-1, -1, -1):
    b += int(a[i])*((2)**j)
    j+=1
print(b)
