
#! Import Modules and The Standard Library

# Solves a lot of common problems

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    "Find the index of a value in a sequence"
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1

# Let's say we want to use this function in our intro.py file
# When we import a file, it runs all the codes from it