
#! Nested Dictionaries and Lists

# Modeling a tic-tac-toe board was fairly simple. The board needed only a single dictionary value with nine key-value pairs
# When modeling more complicated things, we may need dictionaries and lists that contain other dictionaries and lists
    # Lists are useful in containing an ordered series of values
    # Dictionaries are useful for associating keys with values
# Here's a program that uses a dictionary that contains other dictionaries of what items guests are bringing to a picnic
# The totalBrought() function can read this data structure and calculate the total number of an item being brought by all the guests

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples    ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups  ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes  ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies  ' + str(totalBrought(allGuests, 'apple pies')))

# Inside the totalBrought() function:
# 1. The for loop iterates over the key-value pairs in guests
# 2. Inside the loop:
    # 2.a. The string of the guest's name is assigned to k
    # 2.b. The dictionary of picnic items they're bringing is assigned to v
# 3. If the item parameter exists as a key in this dictionary, its value (the quantity) is added to numBrought
    # 3.a. If it does not exist as a key, the get() method returns 0 to be added to numBrought

# This seems like a simgple thing to model and you wouldn't need a program for, but...
    # ...this same totalBrought() function could easily handle a dictionary that contains thousands of guests bringing thousands of different picnic items
# So having this information in a data structure along with the totalBrought() function saves a lot of time

# You can model things wtih data structures in whatever way you like, as long as the rest of the code in your program can work with the data model correctly
# When beginning programming, don't worry too much about the "right" way to model data
    # More exp. = more efficient models, but the important thing is that the data model works for your program's needs


#! Summary

# We learned about dictionaries in this chapter
# Lists and dictionaries are values that can contian multiple values, including other lists and dictionaries.
# Dictionaries are useful because you can map one item (the key) to another (the value), as opposed to lists which simply contain a series of values in order
# Values inside a dictionary are accessed using square brackets (like with lists)
    # Instead of an integer index, dictinoaries can have keys of a variety of data types: integers, floats, strings, tuples
# By organizing a program's values into data structures you can create a representation of real-world objects
    # ex. Tic-Tac-Toe board
    