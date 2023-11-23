
#! Finding Patterns of Text with Regular Expressions

# The previous phone-number finding program works, but uses a lot of code to do something limited
# The isPhoneNumber() function is 17 lines, but can find only one pattern of phone numbers
# What about a phone number formatted like 415.555.4242 or (415) 555-4242?
# What if the phone number had an extension like 415-555-4242 x99?

# Regexes are descriptions for a pattern of text
# ex. a \d in a regex stands for a digit character - any single numeral from 0-9
    # The regex \d\d\d-\d\d\d-\d\d\d\d is used by python to match the same text pattern as the previous isPhoneNumber() function

# But regex can be much more sophisticated
    # Adding a 3 in braces ({3}) after a pattern is like saying: "Match this pattern three times"
        # ex.  \d{3}- \d{3}- \d{4}

#? Creating Regex Objects

# All regex functions in Python are in the re module

import re

# Passing a string value representing your regex to re.compile() returns a Regex pattern object (a Regex object)
# To create a Regex object that matches the phone number pattern, enter:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#? Matching Regex Objects

# A Regex object's search() method searches the string it is passed for any matches to the regex
# The search() method will return None if the regex pattern is not found in the string
# If found, search() method returns a Match object, which have a group() method that will return the actual matched text from the searched string

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# The mo variable name is just a generic name to use for Match objects

# Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex
# Then we call search() on phoneNumRegex and pass search() the string we want to match for during the search
# The result of the search gets stored in the variable mo
# We know that a Match object will be returned because we know our pattern will be found in the string
    # Knowing that mo contains a Match object and not the null value None, we can call group() on mo to return the match
# Writing mo.group() inside our print() function call displays the whole match: 415-555-4242


#? Review of Regular Expression Matching

# While there are several steps to using regular expressions in Python, each step is fairly simple:

#* 1. Import the regex module with import re
#* 2. Create a Regex object with the re.compile() function (remember to use a raw string)
#* 3. Pass the string you want to search into the Regex object's search() method. This returns a Match object
#* 4. Call the Match object's group() method to return a string of the actual matched text