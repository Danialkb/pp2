a, b = input(), input()
prod, prod1 = 1, 1
for i in a:
    prod *= int(i)
for i in b:
    prod1 *= int(i)

print(a) if prod1 > prod else print(b) 

