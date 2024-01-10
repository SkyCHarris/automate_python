
import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

# Let's say we wanna use find_index function

# Type module name first, then what we want to grab from that module

index = my_module.find_index(courses, 'Math')
print(index)

# That works. It returns 1
# But can get old to keep typing in my_module.find_index everywhere
# We can specify a name we want to use for our imported module

import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

# Can we import the function itself? Yes

from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

# To import multiple functions, variables:

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

# Import everything

from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

# How does it know where to find this module?
# When we import a module, checks mult. locations
# Within a list called cys.path
# Can see this list if we import sys module

from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)

# First value is directy we're running the script from
#* What directories are added?
# 1. Directory containing script we're running
# 2. Directories listed in pythhon path environment variable
# 3. Standard library directories
# 4. Site packages directory for 3rd party packages

# First fix: Add directory to sys.path

from my_module import find_index, test
import sys
sys.path.append('Users/coreyschafer/Desktop/My-Modules')

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)

# But that's not the best approach, cuz we're appending before other imports
# And if we import module and this is hardcoded, would have to change all those

# So, make the change in the python path environment variable
# nano ~/.bash_profile
# export PYTHONPATH="C:\User\etc.\etc."


# Standard Libraries
# Let's say we want to grab a random value from a list of values

import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

# Common mathematical operations

import math

courses = ['History', 'Math', 'Physics', 'CompSci']

rads = math.radians(90)

# Datetime / Calendar

import datetime
import calendar

today = datetime.date.today()

print(calendar.isleap(2017))

# Access to underlying operating system

import os

print(os.getcwd())

# Scan file system, create files, delete files, etc.

# View location of module by printing out its dunder file attribute

import os

print(os.__file__)