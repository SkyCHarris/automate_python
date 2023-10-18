# Lists

# Need to understand the list data type and its cousin, the tuple
# Lists and tuples contain multiple values, making writing programs that handle large amounds of data easier
# Lists can contain other lists, can be used to arrange data into heirarchal structures
# Will also learn about methods, which are functions tied to values of a certain data type

# _____________________

# The List Data Type

# A list is a value that contains multiple values in an ordered sequence

[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
['hello', 3.1415, True, None, 42]
spam = ['cat', 'bat', 'rat', 'elephant']
spam

# The spam variable is still assigned only one value: the list value.
# But the list value itself contains otehr values.
# The value [] is an empty list that contains no values, similar to the '' empty string


# Getting Individual Values in a List with Indexes

# Say you have the list ['cat', 'bat', 'rat', 'elephant'] stored in a variable named spam:
    # spam[0] evaluates to 'cat'
    # spam[1] evaluates to 'bat', and so on
    # The integer inside the square brackets that follows the list is called an index

# The first value in the list is at index 0, second at index 1, and so on
# A list of 4 items has index 3 as the last item's value

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
spam[1]
spam[2]
spam[3]
['cat', 'bat', 'rat', 'elephant'][3]
'Hello, ' + spam[0]
'The ' + spam[1] + ' ate the ' + spam[0] + '.'

# Notice that the expression 'Hello, ' + spam[0] evalutes to 'Hello, ' + 'cat' because spam[0] evalutes to the string 'cat'
# The expression then evalutes to the string value 'Hello, cat'
# You'll get an IndexError if you use an index that exceeds the number of values in your list value

spam = ['cat', 'bat', 'rat,' 'elephant']
spam[10000]

# Indexes can only be integer values, not floats:

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1]
spam[1.0]
spam[int(1.0)]

# Lists can also contain other list values
    # The values in these lists of lists can be accessed using multiple indexes

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[0][1]
spam[1][4]

# The first index dictates which list value to use
# Second index indicates which value within the list value
# If you only use one index, the program prints the full list value at that index


# Negative Indexes

# Indexes start at 0 and go up, but you can use negative integers for the index
# Integer value -1 refers to the last index in a list, -2 refers to the second-to-last index and so on

spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
spam[-3]
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'


# Getting a List from Another List with Slices

# Just as an index can get a single value from a list, a 'slice' can get several values from a list in the form of a new list
# A slice is typed between square brackets, like an index, but has two integers separated by a colon
    # - spam[2] is a list with an index (one integer)
    # - spam[1:4] is a list with a slice (two integers)
# In a slice, the first integers is the index where the slice starts
    # The second integer is the index where the slice ends
# A slice goes up to, but doesn't include, the value at the secon index
# A slice evalutes to a new list value

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
spam[1:3]
spam[0:-1]

# As a shortcut you can leave out one or both of the indexes on either side of the colon in the slice.
    # Leaving out the first index is the same as using 0, the beginning of the list
    # Leaving out the second index

spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
spam[1:]
spam[:]


# Getting a List's Length with the len() Function

# The len() function returns the number of values that are in a list value passed to it

spam = ['cat', 'dog', 'moose']
len(spam)


# Changing Values in a List with Indexes

# Normally a variable name goes on the left side of an assignment statement:
    # ex. spam = 42
# But you can use an index of a list to change the value at that index
    # ex. spam[1] = 'aardvark' MEANS "Assign the value at index 1 in the list spam to the string 'aardvark'"

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
spam[2] = spam[1]
spam
spam[-1] = 12345
spam


# List Concatenation and List Replication

# Lists can be concatenated and replicated, like strings
# The + operator combines two lists to creat ea new list value
# The * operator can be used with a list and an integer value to replicate the list

[1, 2, 3] + ['A', 'B', 'C']
['X', 'Y', 'Z'] * 3
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
spam


# Removing Values from Lists with del Statements

# The del statement will delete values at an index in a list
# All of the values in the list after the deleted value will be moved up one index

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
del spam[2]
spam

# The del statement can also be used on a simple variable to delete it, as if it were an 'unassignment' statement