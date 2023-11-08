
#? Indexing and Slicing Strings

# Strings use indexes and slices the same way lists do
# Think of the string 'Hello, world!' as a list and each character in the string as an item with a corresponding index

# The space and exclamation point are included in the character count, so 'Hello, world! is     13 characters long, from H at index 0 to ! at index 12

spam = 'Hello, world!'
spam[0]
spam[4]
spam[-1]
spam[0:5]
spam[:5]
spam[7:]

# If you specify an index, you'll get the character at that position in the string
# If you specify a range from one index to another, the starting index is included and the ending index is not
# So if spam is 'Hello, world!', spam[0:5] is 'Hello'.
    # The substring you get from spam[0:5] will include everything from spam[0] to spam[4], leaving out the comma at index 5 and the space at index 6
    # This is similar to how range(5) will cause a for loop to iterate up to, but not including, 5
# Note that slicing a string does not modify the original string
    # You can capture a slice from one variable in a separate variable

spam = 'Hello, world!'
fizz = spam[0:5]
fizz

# By slicing and storing the resulting substring in another variable, you can have both the whole string and the substring handy for quick, easy access


#? The in and not in Operators with Strings

# The in and not in operators can be used with strings just like with list values
# An expression with two strings joined using in or not in will evalute to a Boolean True or False

'Hello' in 'Hello, World'
'Hello' in 'Hello'
'HELLO' in 'Hello, World'
'' in 'spam'
'cats' not in 'cats and dogs'

# These expressions test whether the first string (the exact string, case-sensitive) can be found within the second string


#! Putting Strings Inside Other Strings

# Putting strings inside other strings is a common operation in programming
# So far we've been using the + operator and string concatenation to do this

name = 'Al'
age = 4000
'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'

# However, this requires a lot fo tedious typing
# A simpler approach is to use string interpolation, in which the %s operator inside the string acts as a marker to be replaced by values following the string.
# one benefit of string interpolation ist hat str() doesn't have to be called to convert values to strings

name = 'Al'
age = 4000
'My name is %s. I am %s years old.' % (name, age)

# Python 3.6 introduced f-strings, similar to string interpolation except that braces are used instead of %s
    # The expression is placed directly inside the braces
# Like raw strings, f-strings have an f prefix before the starting quotation mark

name = 'Al'
age = 4000
f'My name is {name}. Next year I will be {age + 1}.'

# Remember to include the f prefix, otherwise the braces and their contents will be a part of the string value:

'My name is {name}. Next year I will be {age + 1}.'