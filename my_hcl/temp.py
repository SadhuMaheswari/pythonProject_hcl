'''
from caluclator import add
print(add(1,2))
from  no_of_days import *
print(no_of_days(2))
'''
'''
import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.listdir('my_hcl'))
for file in os.listdir('my_hcl'):
    if file
        print(file)

        '''

def find_drives(self):
    drives = []
    for x in range(65,91):
        if os.path.exists(chr(x)+ ":"):
            drives.append(chr(x))
    return drives