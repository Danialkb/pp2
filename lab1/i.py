for i in range(int(input())):
    x = input()
    if '@gmail.com' in x:
        g = x.replace('@gmail.com', '')
        print(g)