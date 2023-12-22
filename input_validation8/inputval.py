
#! Input Validation

# Input validation code checks that values entered by the user are formatted correctly
# If you want a user to enter their ages, your code shouldn't accept nonsensical answers like:
    # Negative Numbers (outside the range of acceptable integers)
    # Words (wrong data type)

# Input validation can prevent bugs or security vulnerabilities
# Implementing a withdrawFromAccount() function needs to take an argument that is a positive number, for example
    # Subtracting a negative umber will end up adding money!

# Input validation is typically done by repeatedly asking the user to input until they enter valid text

# while True:
#     print('Enter your age:')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric digits.')
#         continue
#     if age < 1:
#         print('Please enter a positive number.')
#         continue
#     break

# print(f'Your age is {age}.')

# When you run this code you'll be prompted for your age until you enter a valid one
# This ensures that by the time the execution leaves the while loop, the age variaable will contain a valid value that won't crash the program later

# However, writing input validation code for every input() call in your program quickly becomes tedious
# You may miss certain cases and allow invalid input to pass through your checks
# We'll learn how to use PyInputPlus module for input validation


#? The PyInputPlus Module

# PyInputPlus contains functions similar to input() for several kinds of data:
    # Numbers
    # Dates
    # Email Addresses
    # etc.
# If the user enters invalid input, like badly formatted dates or numbers outside of intended ranges...
    # ...PyInputPlus will reprompt them for for input just like the code in the previous section did
# PyInputPlus also has other useful features like:
    # A limit for the number of times it reprompts users
    # A timeout if users are required to respond within a time limit

# PyInputPlus is not  apart of the Python Standard Library, so you must install it separately using Pip
# To install:
    # Run pip install --user pyinputplus

import pyinputplus as pyip

#* Functions for different kinds of input in PyInputPlus
# inputStr() -> Like the built-in input() function but has the general PyInputPlus features. Can pass custom validation function to it
# inputNum() -> Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it
# inputChoice() -> Ensures user enters one of the provided choices
# inputMenu() -> Is similar to inputChoice(), but provides a menu with numbered or lettered options
# inputDatetime() -> Ensures user enters a date and time
# inputYesNo() -> Ensures the user enters a "yes" or "no" response
# inputBool() -> Similar to inputYesNo(), but takes a "True" or "False" response and returns a Boolean value
# inputEmail() -> Ensures the user enters a valid email address
# inputFilepath() -> Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists
# inputPassword() -> Is like the built-in input(), but displays* characters as the user types so that passwords, or other sensitive information, aren't displayed on the screen

# These functions will automatically reprompt the user for as long as they enter invalid input:

import pyinputplus as pyip

response = pyipnputplus.inputNum()



