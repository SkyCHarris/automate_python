# Augmented Assignment Operators

# When assigning a value to a variable, you will frequently use the variable itself
    # ex. After assigning 42 to variable 'spam', you increase the value in spam by 1 with this code:

spam = 42
spam = spam + 1
spam

# As a shortcut, use the augmented assignment operators += to do the same thing:

spam = 42
spam += 42
spam

# There are augmented assignment operators for the +, -, *, /, and % operators

# The += operator can also do string and list concatenation
# The *= operator can do string and list replication

spam = 'Hello,'
spam += ' world!'
spam
bacon = ['Zophie']
bacon *= 3
bacon

# ______________________________________


# Methods

# A method is the same thing as a function, except it is 'called on' a value.
    # ex. If a list value were stored in spam, you would call the index() list method on that list like so:
        # spam.index('hello')
# The method part comes after the value, separated by a period
# Each data type has its own set of methods.
    # ex. The list data type has several useful methods for finding, adding, removing, and otherwise manipulating values in a list


# Finding a Value in a List with the index() Method

# List values have an index() method that can be passed to a value.
    # If that value exists in the list, the index of the value is returned
    # If not, Python produces a ValueError error

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')

spam.index('heyas')

spam.index('howdy howdy howdy')

# When there are duplicates of the value in the list, the index of its first appearance is returned

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')


# Adding Values to Lists with the append() and insert() Methods

# To add new values to a list, use the append() and insert() methods.
    # Enter the following to call the append() method on a list value stored in the variable 'spam'

spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam

# The append() method call adds the argument to the end of the list
# The insert() method can insert a value at any index in the list
# The first argument to insert() is the index for the new value
    # The second argument is the new value to be inserted

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam

# Notice that the code is spam.append('moose') and spam.insert(1, 'chicken')
    # NOT spam = spam.append('moose') and spam = spam.insert(1, 'chicken')
# Neither append() nor insert() gives the new value of spam as its return value
    # (The return value of append() and insert() is None). The list is modified in place
# Methods belong to a single data type. The append() and insert() methods are list methods that can be called only on list values, not on strings, integers, etc.

eggs = 'hello'
eggs.append('world')

bacon = 42
bacon.insert(1, 'world')
