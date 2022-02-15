def palindrome (s):
    s1 = s[::-1]
    if s1 == s: print('Palindrome!')
    else: print('Not palindrome!')
palindrome(input())