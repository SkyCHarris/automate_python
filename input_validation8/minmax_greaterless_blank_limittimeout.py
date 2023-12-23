
#? The min, max, greaterThan, and lessThan Keywork Arguments

# The inputNum(), inputInt(), and inputFloat() functions (which accept int and float numbers)...
    # ...also have min, max, greaterThan, and lessThan keyword arguments
# These specify a range of valid values

import pyinputplus as pyip

response = pyip.inputNum('Enter num: ', min=4)
response

response = pyip.inputNum('Enter num: ', greaterThan=4)
response

response = pyip.inputNum('>', min=4, lessThan=6)
response


#? The blank Keyword Argument

# By default, blank input isn't allowed unless the blank keyword argument is set to True

import pyinputplus as pyip
response = pyip.inputNum('Enter num: ')

response = pyip.inputNum(blank=True)
# (blank input entered here)

# Use blank=True if you'd like to make input optional so that the user doesn't need to enter anything


#? The limit, timeout, and default Keyword Arguments

# By default, the PyInputPlus functions will continue to ask the user for valid input forever (as long as the program runs)
# If you want a function to stop asking the user for input after:
    # 1. Certain # of tries -> limit
    # 2. Certin amount of time  -> timeout

# Pass an integer for the limit keyword argument to determine how many attempts a PyInputPlus function will make to receive valid input before giving up
# Pass an integer for the timeout keyword argument to determine how many seconds the user has to enter valid input before PyInputPlus gives up

# If the user fails to enter valid input, these keywrod arguments will cause the function to raise a:
    # 1. RetryLimitException
    # 2. TimeoutException

import pyinputplus as pyip
response = pyip.inputNum(limit=2)

import pyinputplus as pyip
response = pyip.inputNum(timeout=10)

# When you use these keyword arguments and also pass a 'default' keyword argument, the function returns the default value instead of raising an exception

import pyinputplus as pyip
response = pyip.inputNum(limit=2, default='N/A')

# Instead of raising RetryLimitException, the inputNum() funciton simply returns the string 'N/A'
