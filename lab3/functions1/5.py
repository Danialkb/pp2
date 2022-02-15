import itertools 
def permut(s):
    perm = set(itertools.permutations(s))
    for i in perm:
        print(*i, sep='')
permut(input())
# global x
# x = []
# def permut(s, i, j):
#     if i == j:
#         print(s)
#         res = ''.join(s)
#         x.append(res)
#     else:
#         for k in range(i, j):
#             s[i], s[k] = s[k], s[i]
#             print(s[i], s[k])
#             permut(s, i + 1, j)
#             s[i], s[k] = s[k], s[i] 
#             print(s[i], s[k])
# s = list(input())
# permut(s, 0, len(s))
# print(*sorted(set(x)), sep = '\n')