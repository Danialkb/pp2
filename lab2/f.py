mydict = dict()
max = 0
for i in range(int(input())):
    x = list(map(str, input().split()))
    if x[0] not in mydict:
         mydict[x[0]] = int(x[1])
    else:
        mydict[x[0]] += int(x[1])
for k in mydict.values():
    if k > max:
        max = k
for i, j in sorted(mydict.items()):
    if j == max:
        print(i, 'is lucky!')
    else:
        print(f'{i} has to receive {max-j} tenge')