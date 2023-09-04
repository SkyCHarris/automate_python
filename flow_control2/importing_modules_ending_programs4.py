# Importing Modules

# -All Python programs can call a basic set of functions, called built-in functions
#   -incl. print(), input(), len(), etc.
# -Python also comes with a set of modules called the 'standard library'
#   -Each module is a Python program that contains a related group of functions that can be embedded in your programs

# -Before using the functions in a module, you must import the module wtih an 'import' statement
# -An import statement consists of:
# 1. The import keyword
# 2. The name of the module
# 3. Optionally, more module names, as long as they are separated by commas

import random
for i in range(5):
    print(random.randint(1, 10))

# from Import Statements

# -An alternative form of the import statement: from -> module name -> import -> star

from random import *

# -With this form of import statement, calls to functions in random will not need the random. prefix

# __________________________

# Ending a Program Early with the sys.exit() Function

# -You can cause a program to terminate or exit before the last instruction by calling the sys.exit() function
#   -Because this function is in the sys module, you have to import sys before your program can use it

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')