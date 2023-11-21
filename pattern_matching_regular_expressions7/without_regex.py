
#! Pattern Matching with Regular Expressions

# Regular Expressions go one step further thank ctrl-f:
    # They allow you to specify a pattern of text to search for

# Phone numbers are ex. 555-918-6920
# Email ex. uses @
# Website ex. periods . and forward slashes /
# News headlines ex. title case
# Hashtags ex. #, no spaces

# Regular expressions are helpful, though few non-programmers know about them
    # But even Microsoft Word or OpenOffice have find and replace features based on regex

# In this chapter, write a program to find text patterns without using regex, then see how regex can unbloat our code
# Basic matching with regex, string substition, creating character classes
# Finally, write a program that can auto-extract phone numbers and email addresses from a block of text


#? Finding Patterns of Text Without Regular Expressions

# Say you want to find an American phone number in a string
    # You know the pattern: 3 numbers, hyphen, 3 numbers, hyphen, 4 numbers

# Use a function named isPhoneNumber() to check whether a string matches this pattern, returning True/False

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return True
    return True

print("Is 415-555-4242 a phone number?")
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

# The isPhoneNumber function has code that does checks to see whether the string in text is a valid phone #
    # If any of these checks fail, the function returns False

# 1. First, code checks that the string is exactly 12 characters
# 2. Then, checks that area code (first 3 characters) consists of only numeric characters
# 3. The rest of the function checsk that the string follows the pattern of a phone number
    # 3.a. The number must have the first pyhen after the area code
    # 3.b. 3 more numeric characters
    # 3.c. Another hyphen
    # 3.d. 4 more numbers
# 4. If execution gets past all checks, it returns True

# Calling isPhoneNumber() with the argument '415-555-4242' returns True
# Calling isPhoneNumber() with 'Moshi moshi' returns False

# To find a phone number in a larger string, need to add even more code to find the phone number pattern

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return True
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# On each iteration of the for loop, a new chhunk of 12 characters from message is assigned to the variable chunk
    # Ex. On first iteration, i is 0, and chunk is assigned message[0:12] (that is, the string 'Call me at 4')
    # Ex. On the next iteration, i is 1, and chunk is assigned message [1:13] (the string 'all me at 41')
# On each iteration of the for loop, chunk takes on the following values:
    # 'Call me at 4'
    # 'all me at 41'
    # 'll me at 415'
    # l me at 415-'
    # ...and so on

# 1. You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern
# 2. If so, you print the chunk
# 3. Continue to loop through message. Eventually the 12 characters in chunk will be a phone number
# 4. Loop goes through entire string, testing each 12-char piece and printing any chunk it finds that fits isPhoneNumber()
# 5. When finished going through message, we print Done
