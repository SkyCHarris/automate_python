
#! 5 Common Python Mistakes and How to Fix Them

#* 1. Mixing Tabs and Spaces (Indentation Errors)

nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)

#? Solution:
    # Upgrade your editor
    # "Translate tabs to spaces"
    # pylint -> catches these mistakes

#* 2. Naming Python Modules Same as What You're Trying to Import
    
# Module with the same name takes higher priority than standard library modules or modules installed using pip

# ex. Project to create python module to do some math calculations
    
# filename: math.py
# import: from math import radians, sin
    
from math import radians, sin

rads = radians(90)

print(sin(rads))

#? Solution:
    # Rename file
    # Common when can't import from standard library
    # Watch variable names too

#* 3. Mutable Default Arguments

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

# Takes in single employee and employee list as arguments
# Adds employee to list, then prints that list

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

add_employee('Corey')
add_employee('John')

# No existing list provided, should be creating new list
# But it's adding to this new list
# Default arguments are evaluated once at the time it creates the function
    # not creating a new empty list each time we run the function
# Using same list it created when the function was defined (mutables)

#? Solution:

def add_employee(emp, emp_list=None):   # =None
    if emp_list is None:    # runs every time the function is run
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

add_employee('Corey')
add_employee('John')

# Other example:
# Prints time in specific format
# Takes 'time' as an argument, default set to datetime.now()

import time
from datetime import datetime

def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# Doesn't update time like we expect
# Only executes default argument once when the function is declared

#? Solution:
# Move inside of function itself!

import time
from datetime import datetime

def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

#* 4. How Iterators Work / How Iterators are Exhausted

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(names, heroes)

print(identities)

# Corresponding indexes we can use zip function for
# Gives zip object
    # <zip object at 0x000001A27BE63140>

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(names, heroes)

print(list(identities))

for identity in identities:
    print('{} is actually {}!'. format(identity[0], identity[1]))

# Doesn't print the formatted string, just the zip tuple
# Iterators can be exhausted. We can loop through and access values once, but can't do it again!
# We're converting to list, then trying to loop over zip object again
    # But we've exhausted zip object when we converted it to a list

#? Solution:
# Convert to list, print that list, then loop over it
# Lists are not exhausted like other iterators/generators

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))   # convert to list from the start

print(identities)

for identity in identities:
    print('{} is actually {}!'. format(identity[0], identity[1]))


#* Using Asterisk when Importing
    
# Asterisk * imports everything from a given module
    
import os

os.rename(filename)
# rename filename

# We can import functions one at a time, ex:

from os import rename

rename(filename)
# for each additional function we'd want to use, have to add it to import line

from os import rename, remove

# Can use * to import everything

from os import *
# bad practice
# people will wonder where the functions are declared, where they're coming from

# Can also have function names used multiple times:

from html import *
from glob import *

print(escape)
# glob overwrites html

#? Solution

from html import escape as h_escape
from glob import escape as g_escape