
#! 11 Methods of Dictionaries

# 1. values()

from dbm import _ValueType


users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

print(users.values())
# returns iterable that can be used in a for loop, anywhere w/ iterable

# 2. keys()

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

print(users.keys())
# return all the keys in our dictionary, as an iterable

# 3. pop()
# Remove a specified key by passing it into our dictionary

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

users.pop(2)
print(users)
# can assign pop to a variable

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

popped = users.pop(2)
print(popped)

# 4. popitem()
# pops the last item from our dictionary

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

users.popitem()
users.popitem()
print(users)
# can be used multiple times

# 5. copy()

sample_dict: dict = {0: ['a', 'b'], 1: ['c', 'd']}

my_copy: dict = sample_dict.copy()

print(sample_dict)
print(my_copy)

# Verify we have different copies with id method:

sample_dict: dict = {0: ['a', 'b'], 1: ['c', 'd']}

my_copy: dict = sample_dict.copy()

print(id(sample_dict))
print(id(my_copy))

# Changing values will change values for both dictionaries. Ex:

sample_dict: dict = {0: ['a', 'b'], 1: ['c', 'd']}
my_copy: dict = sample_dict.copy()

my_copy[0][0] = '!!!'
print(sample_dict)
print(my_copy)

# To change this behavior, need to use deepcopy()

# 6. get()
# Get value from dictionary w/out raising an exception

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

print(users.get(1))
# specify what to return if value is missing

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

print(users.get(5, 'Missing!'))

# 7. setdefault()
# Tries to grab key/value pair. Creates one if it doesn't exist

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

print(users.setdefault(999, '???'))

# 8. clear()
# Want to start fresh with your dictionary

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

users.clear()
print(users)

# 9. fromkeys()
# Need an iterable to use

people: list[str] = ['Mario', 'Luigi', 'James']
users: dict = dict.fromkeys(people)
print(users)

# Can also pass in default value

people: list[str] = ['Mario', 'Luigi', 'James']
users: dict = dict.fromkeys(people, __value:'Unknown')
print(users)

# 10. items()
# Gives back an iterable that contains tuples of the key/value pair for each item inside dictionary

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
print(users.items())

for k, v in users.items():
    print(k, v)

# 11. update()
# Further modify or expand dict. with new key/value pairs
    
users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users.update({2: 'Bob', 3: 'Jame\'s sister'})

print(users)

# union operator |

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}
users2: dict = {10: 'Spam', 11: 'Eggs'}

print(users | users2 )