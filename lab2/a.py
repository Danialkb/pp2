a = list(map(int,input().split()))
posi = len(a) - 1
for i in range(len(a) - 2, -1, -1):
    if i + a[i] >= posi:
        posi = i
print(1) if posi == 0 else print(0)




# a, b = list(map(int, input().split())), 0
# for i in range(len(a)):
#     posi = b+a[b]+1
#     for j in range(b, posi):
#         print(b+a[b], a[j] + j)
#         if b + a[b] < a[j] + j:
#             b = j
#         elif posi >= len(a):
#             print(1)
#             exit(0)
# print(0)