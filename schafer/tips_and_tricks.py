
#! 10 Python Tips and Tricks for Writing Better Code

#* 1. Ternary Operators (Ternary Conditionals)
# Save you from writing unnecessary code

condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

# Faster way to write this

condition = False

x = 1 if condition else 0
# ternary conditional gives same result

# one-liner doesn't always mean code is better

#* 2. Large Numbers
# Hard to keep track of nums with lots of digits
# Commas work on paper. But in Python we can use underscores instead

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(total)

# output still doesn't have separators.

# Use string formatting!

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')   # use colon to format f'strings

#* 3. Context Manager (Opening/Closing Files)
# Manually managing resources, remembering to manually close file, should set off auto-alarms
# 'Code Smell'

f = open('test.txt', 'r')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Context Managers manage resources for you so you don't need to yourself

with open('test.txt', 'r') as f:
    file_contents = f.read()    # read in contents of file w/in context manager

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
# no need to manually close down file

# Train yourself to know when you need a context manager

#* 4. Enumerate
# When you need a counter while looping over something
# When you want to keep a count of what num you're currently on

# Bad example
names = ['Corey', 'Chris', 'Dave', 'Travis']

index = 0
for name in names:
    print(index, name)
    index += 1

# Use enumerate
# Returns index and value that we're looping over
# Use unpacking to grab those values
    
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names):
    print(index, name)

# can pass in start value if you don't want to start at 0
    
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names, start=1):   # start value to mark where you want to start in the loop
    print(index, name)

#* 5. Using Bad Code Because Unaware a Function Exists
    
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# want to loop over two lists at once
# access the first value of each list, then second value of each list

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# not really intuitive
    
# Use zip() Function
    # loop over two values at once
    # returns both values of the loop at once
    
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

# zip actually works for more than one list
    
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# Zip to go to longest list
# ziplongest() ?
    
# zip is returning a tuple of 3 items here
# we're unpacking them by setting 3 variables

# We can access that single tuple if we want
    
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for value in zip(names, heroes, universes): # value accesses same tuple kinda?
    print(value)
    
#* 6. Unpacking
# Some different ways we can unpack different values
    
# Normal
# How we are normally used to creating a list or a tuple
# Unpack all the values into different variables
    
a, b = (1, 2)

print(a)
print(b)
# unpacking 2 values into 2 diff. variables

# Only want to use 'a' value
# Python convention - use _ (underscore) as the name

a, _ = (1, 2)

print(a)
print(b)

# _ tells Python or anyone else that we're not planning on using that variable elsewhere

# What if what we're trying to unpack doesn't include as many values as the variables that we're trying to set?
# Error

a, b, c = (1, 2)

print(a)
print(b)
# ValueError: not enough values to unpack

# What if more values than variables?

a, b, c = (1, 2, 3, 4, 5)

print(a)
print(b)
# ValueError: too many values to unpack

# Asterisk * to set c to the rest of the values

a, b, *c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)
# to ignore those values, use underscore

a, b, *_ = (1, 2, 3, 4, 5)

print(a)
print(b)
# print(c)

# Use same syntax with additional variable added onto the end

a, b, *c, d = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)
print(d)
# a = 1, b = 2, c = [3, 4], d = 5

#* 7. Getting and Setting Attributes on a Certain Object
# Can dynamically add attributes and values to objects with classes

# Add attributes/methods
class Person():
    pass

person = Person()

person.first = "Corey"
person.last = "Schafer"

print(person.first)
print(person.last)

# Attribute we want to set is value of another variable?
# take value of first_key variable and use it as a an attribute for our object
# set attr. to value of first_val
# run same print statement as before
    # but have the new value

# Use setattr

class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, 'first', 'Corey')

print(person.first)

# When using setattr, can use variables


class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)   # include variables here

print(person.first)

# getattr() to get a value

class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, 'first', 'Corey')

first = getattr(person, first_key)

print(first)

# Old example
# loop over items in dict. and add them as attr. to person object

class Person():
    pass

person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

# Print attributes in a loop as well

class Person():
    pass

person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

#* 8. Input Secret Information
# pre. keep sensitive information in environment variables
# What if you need to type in a password for your script?
    
# Built-in Function -> getpass()
    
# Bad Example
username = input('Username: ')
password = input('Password: ')

print('Logging In...')

# getpass()
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging In...')

#* 9. Run Python with -m Option
# Venv: python -m venv my_env

# What is -m actually doing?
    # Search sys.path for the named module, and execute its contents as the named module
    # Everything after -m (module) are arguments for that module

# Why not write like other scripts?
    # python3 password.py exists in our current directory
    # other scripts do not exist in current directory
    # can run like this:
        # python3 -m password (don't inlcude .py)
    # searches sys.path for password module, runs it
        # current directory is included in the sys.path

# How to know which arguments it can take?
    # You can import anything on your sys.path

#* 10. Learn More About Objects with Built-in Functions

# import smtpd
# help(smtpd)

# Just wanna know attr/methods?

# from datetime import datetime
# dir(datetime)




