import math
import time
a, b = int(input()), int(input())
print(f'I am waiting for {b} miliseconds...')
time.sleep(b/1000)
print(math.sqrt(a))