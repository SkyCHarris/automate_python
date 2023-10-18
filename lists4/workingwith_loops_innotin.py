# Working with Lists

# It's tempting to create many individual variables to store a group of similar values
# ex.

catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catname5 = 'Fat-tail'
catName6 = 'Miss Cleo'

# This isn't a great way to write code.
# If the number of cats changes, the program will not be able to store more cats than you have variables for
# With duplicate or nearly identical code, consider reducing

print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
# etc. etc.
print('The cat names are:')
print(catName1 + '' + catName2 + '' + catName3) # etc.

# Instead of using multiple, repetitive variables you can use a single variable that contains a list value
# This new version of the program uses a single list and can store any number of cats that the user types in

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)


# Using for Loops with Lists

# We learned about using loops to execute a block of code a certain number of times
# A for loop repeats the code block once for each item in a list value

for i in range(4):
    print(i)

# The return value from range(4) is a sequence value that Python considers similar to [0, 1, 2, 3].
# This program has the same output as the previous one

for i in [0, 1, 2, 3]:
    print(i)

# This loop actually loops through its clause with the variable i set to a successive value in the [0, 1, 2, 3] list in each iteration
# Common technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Using range(len(supplies)) in this for loop is handy because:
    # 1. The code in the loop can access the index (as the variable i)
    # 2. The value at that index (as supplies[i])


# The in and not in Operators

# You can determine whether a value is or isn't in a list with the in and not in operators.
# in and not in are used in expressions, and connect two values:
    # 1. A value to look for in a list
    # 2. The list where it may be found
# These expressions will evalute to a Boolean value

'howdy' in ['hello', 'hi', 'howdy', 'heyas']
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
'howdy' not in spam
'cat' not in spam

# The following example lets the user type in a pet name,
# then check to see whether the name is in a list of pets

myPets = ['Zophie', 'Pooka', 'Fat-tail']
petName = input("Enter a pet name:")
petName in [myPets]

if petName in myPets:
    print(petName + ' is in your list of pets!')
elif petName not in myPets:
    print(petName + ' is not in your list of pets')


# The Multiple Assignement Trick

# The multiple assignment trick (tuple unpacking):
    # A shortcute letting you assign multiple variables with the values in a list in one line of code

# Instead of:

cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# Use:

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

# The number of variables and length of list must be exactly equal to avoid ValueError:


# Using the enumerate() Function with Lists

# Instead of using the range(len(someList)) technique with a for loop to obtain the integer index of the items in the list...
    # Call the enumerate() function
# On each iteration of the loop enumerate() will return two values: 
    # 1. The index of the item in the list
    # 2. The item in the list itself

# range(len(someList)) format:

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# enumerate() is useful if you need both the item and the item's index in the loop's block


# Using the random.choice() and random.shuffle() Functions with Lists

# The 'random' module has a couple functions that aceept lists for arguments
# random.choice() function returns a randomly selected item from the list

import random

pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)
random.choice(pets)
random.choice(pets)

# random.choice(someList) is a like a shorter form of someList[random.randint(0, len(someList - 1]

# random.shuffle function reorders the items in a list.
# It modifies the list in place rather than returning a new list

import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
people