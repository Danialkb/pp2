from datetime import *

a = datetime(2000, 6, 4, 11, 59, 15)

b = datetime(2022, 4, 21, 18, 25, 30)

c = a - b

print(c)
print('Difference in seconds:', c.seconds)