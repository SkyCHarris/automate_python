
#! Sequence Data Types

# Lists aren't the only data types that represent ordered sequences of values
# Strings and lists are actually similar if you consider a string to be a 'list' of single text characters
# Python's sequence data types include:
    # Lists
    # Strings
    # Range objects returned by range()
    # Tuples
# Many things you can do with lists can also be done wtih strings and other values of sequence types:
    # Indexing
    # Slicing
    # Using with for loops
    # Using with len()
    # Using with in and not in operators

name = 'Zophie'
name[0]
name[-2]
name[0:4]
'Zo' in name
'z' in name
'p' not in name

for i in name:
    print('***' + i + '***')


#? Mutable and Immutable Data Types

# Lists and strings are different in an important way:
    # List value is a mutable data type
        # It can have values added, removed, or changed
    # String is immutable
        # It cannot be changed

name = 'Zophie a cat'
name[7] = 'the'

# The proper way to mutate a string is to use slicing and concatenation to build a new string by copying parts of the old string

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
newName

# We used [0:7] and [8:12] to refer to the characters that we don't wish to replace
# Notice the original 'Zophie a cat' string is not modified, because strings are immutable
# Although a list value is mutable, the second line in the following code does not modify the list eggs:

eggs = [1, 2, 3]
eggs = [4, 5, 6]
eggs

# The list value in eggs isn't being changed
    # Instead, an entirely new and different list value [4, 5, 6] is overwriting the old list value [1, 2, 3]
# If you want to modify the original list to contain [4, 5, 6]

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs

# Changing a value of a mutable data type changes the value in place, since the variable's value is not replaced with a new list value


#? The Tuple Data Type

# The tuple data type is almost identical to the list data type, except for in two ways:
    # 1. Tuples are typed with parentheses ( and ), instead of square brackets [ and ]
    # 2. Tuples, like strings, are immutable
        # Cannot have their values modified, appended, or removed

eggs = ('hello', 42, 0.5)
eggs[0]
eggs[1:3]
len(eggs)

# 2. 
eggs = ('hello', 42, 0.5)
eggs[1] = 99

# If you have only one value in  your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses
    # Otherwise Python will think you've just typed a value inside regular parentheses
    # The comma lets Python know this is a tuple value

type(('hello',))
type(('hello'))

# You can use tuples to convey to anyone reading yoru code that you don't intend for that sequence of values to change
# If you need an ordered sequence of values that never changes, use a tuple
# A second benefit to tuples instead of lists is that because they are immutable and their contents don't change, Python can implement some optimizations that make code using tuples slightly faster than code using lists

# "sequence data types, mutable and immutable, tuples, converting types with list and tuple functions"
#? Converting Types with the list() and tuple() Functions

# Just like how str(42) will return '42', the string representation of the integer 42...
    # The functions list() and tuple() will return list and tuple versions of the values passed to them

tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')

# Convertin a tuple to a list is handy if you need a mutable version of a tuple value