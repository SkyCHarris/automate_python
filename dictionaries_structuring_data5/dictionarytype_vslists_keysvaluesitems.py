
#! Dictionaries and Structuring Data

# The dictionary data type provides a flexible way to access and organize data
# Combining dictionaries with your knowledge of lists from the previous chapter will help create a data structure model of a tic-tac-toe board

#! The Dictionary Data Type

# Like a list, a dictionary is a mutable collection of many values
# Unlike indexes for lists, indexes for dictionaries can use many different data types, not just integers
    # Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair

# A dictionary is typed with braces {}

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# This assigns a dictionary to the myCat variable
    # This dictionary's keys are 'size, 'color', and 'dispotition'.
    # The values for these keys are 'fat', 'gray', and 'loud', respectively
# You can access these values through their keys:

myCat['size']
'My cat has ' + myCat['color'] + ' fur.'

# Dictionaries can still use integer values as keys, just like lists use integers for indexes
    # But they do not have to start at 0 and can be any  number

spam = {12345: 'Luggage Combination', 42: 'The answer'}


#? Dictionaries vs. Lists

# Unlike lists, items in dictionaries are unordered.
    # The first item in a list named spam would be spam[0]
    # But there is no 'first' item in a dictionary
# The order of items matters for determing whether two lists are the same.
    # It does not matter in what order the key-value pairs are typed in a dictionary

spam = ['cats', 'dogts', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham

# Because dictionaries are not ordered, they can't be sliced like lists
# Trying to access a key that does not exist in a dictionary will result in a KeyError error message, like a list's "out-of-range" IndexError
# Notice the error message that shows up because ther is no color key:

spam = {'name': 'Zophie', 'age': 7}
spam['color']

# Though dictionaries are unordered, having arbitrary values for the keys allows you to organize your data in powerful ways
# Say you want your program to store data about your friends' birthdays
    # You can use a dicitonary with the names as keys and the birthdays as values

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# All the data you enter in this program is forgotten when the program terminates
# You'll learn how to save data to files on the hard drive in Chapter 9

#? Ordered Dictionaries in Python 3.7

# While still not ordered and have no "first" key-value pair...
    # ...dictionaries in Python 3.7 and later will remember the insertion order of their key-value pairs if you create a sequence value from them
# Notice the order of items in the lists made from the eggs and ham dictionaries matches the order in which they were entered:

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
list(eggs)

ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
list(ham)

# These dictionaries are still unordered. You can't access items in them using integer indexes like eggs[0] or ham[2].
# Don't rely on this as older versions of Python don't remember the insertion order of key-value pairs
# Notice how hte list doesn't match the insertion order of the dictionary's key-value pairs when running this code in 3.5

#? The keys(), values(), and items() Methods

# There are three dictionary methods that will return list-like values of the dictionary's keys, values, or both keys and values:
    # keys(), values(), items()
# The values returned by these methods are not true lists: 
    # They cannot be modified and do not have an append() method
# But these data types (dict_keys, dict_values, dict_items) can be used in for loops

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

# Here, a for loop iterates over each of the values in the spam dictionary
# A for loop can also iterate over the keys or both keys and values:

spam = {'color': 'red', 'age': 42}
for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

('color', 'red')
('age', 42)

# When you use the keys(), values(), and items() methods, a for loop can iterate over they keys, values, or key-value pairs in a dictionary
# Notice that the values in the dict_items value returned by the items() method are tuples of the key and value

# If you want a true list from one of these methods, pass its list-like return value to the list() function:

spam = {'color': 'red', 'age': 42}
spam.keys()
list(spam.keys())

# The list(spam.keys()) line takes the dict_keys value returned from keys() and passes it to list(), which then returns a list value of ['color', 'age']
# You can also use the multiple assignment trick in a for loop to assign the key and value to separate variables:

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))