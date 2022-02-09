from math import *
global x, y
x, y = map(int, input().split())
def sortfunct(a):
    return sqrt((a[0] - x) ** 2 + (a[1] - y) ** 2)
clsP = []
for i in range(int(input())):
    x1, y1 = map(int, input().split())
    tupl = tuple((x1, y1))
    clsP.append(tupl)
clsP.sort(key=sortfunct)
for i in clsP:
    print(*i)