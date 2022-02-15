def spygame(a):
    s = ''
    for i in a:
        if i == 0 or i == 7: 
            s += str(i)
    if '007' in s:
        return True
    else: return False
print(spygame(list(map(int, input().split()))))