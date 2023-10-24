
#? The startswith() and endswith() Methods

# The startswith() and endswith() methods return True if the string value they are called on begins or ends with the string passed to the method
    # Otherwise they return False

'Hello, world!'.startswith('Hello')
'Hello, world!'.endswith('world!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')
'Hello, world!'.startswith('Hello, world!')
'Hello, world!'.endswith('Hello, world!')

# These methods are useful alternatives to the == equals operator if you need to check only whether the first or last part of the string, rather than the whole thing, is equal to another string


#? The join() and split() Methods

# The join() method is useful when you have a list of strings taht need to be joined together into a single string value
# The join() method is called on a string, gets passed a list of strings, and returns a string
    # The returned string is the concatenation of each string in the passed-in list

', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])
'ABC'.join(['My', 'name', 'is', 'Simon'])

# Notice that the string join() calls on is inserted between each string of the list argument
    # ex. When join(['cats', 'rats', 'bats']) is called on the ', ' string, the returned string is 'cats, rats, bats'.
# Remember that join() is called on a string value and is passed a list value (it's easy to do this the other way around)

# The split() method does the opposite: it's called on a string value and returns a list of strings:

'My name is Simon'.split()

# By default, the string 'My name is Simon' is split wherever whitespace characters such as space, tab, or newline characters are found
    # These whitespace characters are not included in the strings in the returned list
# You can pass a delimiter string to the split() method to specify a different string to split upon

'MyABCnameABCisABCSimon'.split('ABC')
'My name is Simon'.split('m')

# A common use of split() is to split a multiline string along the newline characters:

spam = '''
Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment.

Please do not drink it.
Sincerely,
Bob
'''
spam.split('\n')

# Passing split() the argument '\n' lets us split the multiline string stored in spam along the newlines and return a list in which each item corresponds to one line of the string


#? Splitting Strings with the partition() Method

# The partition() string method can split a string into the text before and after a separator string
# This method searches the string it is called on for the separator string it is passed, and returns a tuple of three substrings for the "before", "separator", and "after" substrings

'Hello, world!'.partition('w')
'Hello, world!'.partition('world')

# If the separator string you pass to partition() occurs multiple times in the string that partition() calls on, the method splits the string only on the first occurrence:

'Hello, world!'.partition('o')

# If the seperator string can't be found, the first string returned in the tuple will be the entire string, and the other two strings will be empty:

'Hello, world!'.partition('XYZ')

# You can use the multiple assignment trick to assign the three returned strings to three variables:

before, sep, after = 'Hello, world!'.partition(' ')
before
sep
after

# The partition method is useful for splitting a string whenever you need the parts before, including, and after a particular separator string


#? Justifying Text with the rjust(), ljust(), and center() Methods

# The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text
# The first argument to both methods is an integer length for the justified string

'Hello'.rjust(10)
'Hello'.rjust(20)
'Hello, World'.rjust(20)
'Hello'.ljust(10)

# 'Hello'.rjust(10) says that we want to right-justify 'Hello' in a string of total length 10.
# 'Hello' is five chracters, so the five spaces will be added to its left giving us a string of 10 characterw tih 'Hello' justified right
# An optional second argument to rjust() and ljust() will specify a fill character other than a space character

'Hello'.rjust(20, '*')
'Hello'.ljust(20, '-')

# The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right

'Hello'.center(20)
'Hello'.center(20, '=')

# These methods are especially useful when you need to print tabular data that has correct spacing

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# In this program we define a printPicnic() method that will take in a dicitonary of information and use center(), ljust(), and rjust() to display that information in a neatly aligned table-like format
# The dictionary that we'll pass to printPicnic() is picnicItems.
    # In picnicItems we have 4 sandwiches, 12 apples, 4 cups, and 8,000 cookies
    # We want to organize this information into two columns, with the name of the item on the left and the quantity on the right
# To do this we decide how wide we want the left and right columns to be
    # Along with our dictionary, we pass these values to printPicnic()
# The printPicnic() function takes in a dictionary, a leftWidth for the left column of a table, and a rightWidth for the right column
    # It prints a title, PICNIC Items, centered above the table
    # Then it loops through the dictionary, printing each key-value pair on a line with the key justified left and padded by periods
    # And the value justified right and padded by spaces
# After defining printPicnic(), we define the dicitonary picnicItems, and call printPicnic() twice, passing it different widths for the left and right table columns
# When you run this program the picnic items are displayed twice
    # The first time the left column is 12 characters wide, and the right column is 5 characters wide
    # The second time they are 20 and 6 characters wide, respectively
# Using rjust() and ljust() and center() lets you ensure that strings are neatly aligned, even if you aren't sure how many characters long your strings are


#? Removing Whitespace with the strip(), rstrip() and lstrip() Methods

# Sometimes you may want to strip off whitespace characters (space, tab, and newline) from the left, right or both sides of a string
# strip() string method returns a new string without any whitespace characters at the begnning or end
# lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively

spam = '    Hello, World    '
spam.strip()
spam.lstrip()
spam.rstrip()

# Optionally, a string argument will specify which characters on the ends should be stripped

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

# Passing strip() the argument 'ampS' will tell it to strip occurences of a, m, p, and capital S from the ends of the string stored in spam
# The order of the characters in the string passed to strip() does not matter: strip('ampS') will do the same thing as strip('mapS') or strip('Spam')
