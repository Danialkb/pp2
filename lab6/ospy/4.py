with open('test1.txt', 'r', encoding='utf8') as f:
    counter = sum(1 for line in f)
    
print(counter)