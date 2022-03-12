import os

mypath = input()

print('Existing:', os.path.exists(mypath))

if os.path.exists(mypath):
    print('Filename:', os.path.basename(mypath))
    print('Dirname:', os.path.dirname(mypath))
# Input:
# C:\Users\User\pp projects\pp2 zhylan\lab6\ospy\3.py

# Output:
# Existing: True
# Filename: 3.py
# Dirname: C:\Users\User\pp projects\pp2 zhylan\lab6\ospy