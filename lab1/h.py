a, b, c = input(), input(), []
for i in range(len(a)):
    if a[i] == b:
        c.append(i) 
        break
for i in range(len(a)-1, c[0], -1):
    if a[i] == b:
        c.append(i) 
        break
for i in range(len(c)):
    print(c[i], end = ' ')