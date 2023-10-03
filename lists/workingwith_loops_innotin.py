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