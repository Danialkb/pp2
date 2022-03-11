from math import *

n, len_side = int(input()), int(input())

S =  pow(len_side, 2) * n / 4 * (tan(pi/n)) 
print(ceil(S))