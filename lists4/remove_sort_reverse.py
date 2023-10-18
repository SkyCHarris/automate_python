# Removing Values from Lgit l ists with the remove() Method

# The remove() method is passed the value to be removed from the list it is called on

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam

# Attempting to delete a value that doesn't exist in the list will result in a ValueError error

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')

# If the value appears multiple times in the list, only the first instance of the value will be removed


# Sorting the Values in a List with the sort() Method

# Lists of number values or lists of strings can be sorted with the sort() method

spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order

spam.sort(reverse=True)
spam

# Three things you should note about the sort() method:
    # 1. sort() method sorts the list in place, don't try to capture the return value w/ smthing like spam = spam.sort()
    # 2. You can't sort lists that have both number valu3es and string values
    # 3. sort() uses "ASCIIbetical order" rather than actual alphabetical order. Uppercase letters come before lower-case letters

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort
spam

# Should you need to sort values in regular alphabetical order, pass str.lower for the keyword argument in the sort() method call:

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.lower)
spam

# This causes sort() function to treat all items int he list as if they were lowercase, without actually changing the values in the list


# Reversing the Values in a List with the reverse() Method

# If you need to quickly reverse the order of the items in a list, you can call the reverse() list method

spam = ['cat', 'dogt', 'moose']
spam.reverse()
spam

# Like the sort() list method, reverse() doesn't return a list