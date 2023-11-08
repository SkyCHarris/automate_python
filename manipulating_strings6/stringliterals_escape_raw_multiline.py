
#! Manipulating Strings

# Text is one of the most common forms of data your programs will handle
# We know how to concatenate two string values with the + operator, but there's more
    # Extract partial strings from string values
    # Add or remove spacing
    # Convert letters to lowercase or uppercase
    # Check strings are formatted correctly
    # Even write Python code to access the clipboard for copying and pasting text

#! Working with Strings

# Let's look at some of the ways Python let's you write, print, and access strings in our code


#? String Literarls

# Typing string values in Python code is straightforward
    # They begin and end with a single quote.
    # But then, how to use a quote inside a string?
# Fortunately there are mulitple ways to type strings

#* Double Quotes

# Strings can begin and end with double quotes, just as they can with single quotes
    # One benefit of using double quotes is that the string can have a single quote character in it

spam = "That is Alice's cat."

# Since the string begins with a double quote, Python knows that the single quote is part of the string and not markign the end of the string
# However, if you need to use both single quotes and double quotes, you'll need to use escape characters

#* Escape Characters

# An escape character lets you use characters that are otherwise impossible to put into a string
# Escape character consists of a backslash (\) followed by the character you want to add to the string
    # (Despite consisting of two characters, it is commonly referred to as a singular escape character)
    # ex. The escape character for a ginle quote is \'
# Use this inside a string that begins and ends with single quotes

spam = 'Say hi to Bob\'s mother.'

# Python knows that since the single quote in Bob\'s has a backslash, it is not a single quote meant to end the string value
# The escape characters \' and \" let you put single quotes or double quotes inside your strings, respectively

# \'    Single quote
# \"    Double Quote
# \t    Tab
# \n    Newline (line break)
# \\    Backslash

print("Hello there!\nHow are you?\nI\'m doing fine.")

#* Raw Strings

# You can place an r before the beginning quotation mark of a string to make it a raw string
# A raw string completely ignores all escape characters and prints any backslash that appears in the string

print(r'That is Carol\'s cat.')

# Because this is a raw string, Python considers the backslash as part of the string and not as the start of an escape character
# Raw strings are helpful if you are typing string values that contain many backslashes, such as the strings used for Windows file paths like r'C:\Users\Al\Desktop' or regular expressions described in the next chapter

#* Multiline Strings with Triple Quotes

# While you can use the \n escape character to put a newline into a string, it is often easier to use multiline strings
# A multiline string in Python begins and ends with either three single quotes or three double quotes
# Any quotes, tabs, or newlines in between the "triple quotes" are considered part of the string
    # Python's indentation rules for blocks do not apply to lines inside a multiline string

print('''Dear Alice,
      
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
Sincerely,
Bob''')

# Notice that the single quote character in Eve's does not need to be escaped
# Escaping single and double quotes is optional in multiline strings
# The following print() call would print identical text but doesn't use a multi-line string:

print('Dear Alice, \n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion. \n\nSincerely, \nBob')

#* Multiline Comments

# While the hash character (#) marks the beginning of a comment for the rest of the line, a multiline string is often used for comments that span multiple lines

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')