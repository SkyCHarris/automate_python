
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
