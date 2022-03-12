import os

mypath = input()
if os.access(mypath, os.F_OK):
    os.remove(mypath)
    print('Removed!')
else:
    print('NO SUCH FILE!!!!!!!!')