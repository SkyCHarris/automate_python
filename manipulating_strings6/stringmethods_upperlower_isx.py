
#! Useful String Methods

# Several string methods analyze strings or create transformed string values
# This section describes the methods you'll be using most often:

#? The upper(), lower(), isupper(), and islower() Methods

# The upper() and lower() string methods return a new string where all the letters in the original string have been converted to uppercase or lowercase
# Nonletter characters in the string remain unchanged

spam = 'Hello, world!'
spam = spam.upper()
spam
spam = spam.lower()
spam

# Note that these methods do not change the string itself but return new string values
# If you want to change the origina string, you have to call upper() or lower() on the string and then assign the new string to the variable where the original was stored
# You must use spam = spam.upper() to change the string in spam instead of simply spam.upper()
    # (Just like if a variable eggs contains the value 10. Writing eggs + 3 does not change the value of eggs, but eggs = eggs + 3 does.)

# The upper() and lower() methods are helpful if you need to make a case-insensitive comparison
    # ex. The strings 'great' and 'GREat' are not equal to each other
        # But in the following program, it doesn't matter whether the user types Great, GREAT, or grEAT, because the string is first converted to lowercase:

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# When you run this program, the question is displayed, and entering a varition on great, such as GREat, will still give the output 'I feel great too'.
# Adding code to your program to handle variations or mistakes in user input, such as inconsistent capitalization, will make your programs easier to use

# The isupper() and islower() methods will return a Boolean True value if the string has at least one letter, and all the letters are uppercase or lowercase, respectively
    # Otherwise the method returns False

spam = 'Hello, world!'
spam.islower()
spam.isupper()
'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()

# Since the upper() and lower() string methods themselves return strings, you can call string methods on THOSE returned string values as well
# Expressions that do this will look like a chain of method calls

'Hello'.upper()
'Hello'.upper().lower()
'Hello'.upper().lower().upper()
'HELLO'.lower()
'HELLO'.lower().islower()


#? The isX() Methods

# Along with islower() and isupper(), there are several other string methods that have names beginning with the word 'is'
# These methods return a Boolean value that describes the nature of the string

    # isalpha() -> Returns True if the string consists only of letters and isn't blank
    # isalnum() -> Returns True if the string consists only of letters and numbers and is not blank
    # isdecimal() -> Returns True if the string consists only of numeric characters and is not blank
    # isspace() -> Returns True if the string consists only of spaces, tabs, and newlines and is not blank
    # istitle() -> Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

'hello'.isalpha()
'hello123'.isalpha()
'hello123'.isalnum()
'hello'.isalnum()
'123'.isdecimal()
'   '.isspace()
'This Is Title Case'.istitle()
'This Is Title Case 123'.istitle()
'This Is not Title Case'.istitle()
'This is NOT Title Case Either'.istitle()

# The isX() string methods are helpful when you need to validate user input
    # ex. The following program repeatedly asks users for their age and a password until they provide valid input

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# In the first while loop we ask the user for their age and store their input in age
    # If age is a valid (decimal) value, we break out of this first while loop and move on to the second, which asks for a password
        # Otherwise we inform the user that they need to enter a number and again ask them to enter their age
# In the secon while loop we ask for a password, store the user's input in password, and break out of the loop if the input was alpha-numeric
    # If it wasn't, we're not satisfied, so we tell the user the password needs to be alphanumerica and again ask them to enter a password

# Calling isdecimal() and isalnum() on variables, we're able to test whether the values stored in those variables are decimal or not, alphanumeric or not
# These tests help us reject the unwanted inputs and accepted the desirable ones