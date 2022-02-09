demons, hunters, kolvo = dict(), dict(), 0
for i in range(int(input())):
    a = list(input().split())
    if a[1] not in demons:
        demons[a[1]] = 1
    else:
        demons[a[1]] += 1
for i in range(int(input())):
    a = list(input().split())
    if a[1] not in hunters:
        hunters[a[1]] = int(a[2])
    else:
        hunters[a[1]] += int(a[2])
for i in demons.keys():
    if i in hunters.keys():
        demons[i] -= hunters[i]
    if demons[i] > 0:
        kolvo += demons[i] 
print("Demons left:", kolvo)
