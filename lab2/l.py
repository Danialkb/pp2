s, stack, closed, opened = input(), [], '})]', '{(['
for i in s:
    if i in opened:
        stack.append(i)
    elif i in closed:
        pos = closed.index(i)
        if len(stack) != 0 and stack[len(stack) - 1] == opened[pos]:
            stack.pop()
        else:
            print('No')
            exit(0)
if len(stack) == 0:
    print('Yes')
else:
    print('No')