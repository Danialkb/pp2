from dan import *
a = list(map(int, input().split()))
print(*list(filter(lambda x: (is_prime(x)), a)))