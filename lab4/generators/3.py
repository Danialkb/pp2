def delimost(n):
    for i in range(n):
        if i%12 == 0:
            yield i

for j in delimost(int(input())):
    print(j, end=' ')

#     another way:
# 
# def delimost(n):  
#     return [i for i in range(n) if i % 12 == 0]
# print(delimost(int(input())))
