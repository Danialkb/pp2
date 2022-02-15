from math import *

def is_even(a):
    if a % 2 == 0:
        return True
    else: return False


def is_prime (a):
    if a == 1:
        return False
    for i in range (2, int(sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True


def histogram(a):
    for i in range(len(a)):
        a[i] = '*'*a[i]
    return a


def palindrome (s):
    s1 = s[::-1]
    if s1 == s: return True
    else: return False

def V_of_Sphere (R):
    return (4/3) * pi * (R)**3


def toC (F):
    C = (F-32) * 5/9
    return C


def filter_prime(b):
    c = []
    for i in range(len(b)):
        if is_prime(b[i]) == True:
            c.append(b[i])
    return c


def reversed(s):
    c = []
    for i in range(len(s)-1, -1, -1):
        c.append(s[i])
    return c