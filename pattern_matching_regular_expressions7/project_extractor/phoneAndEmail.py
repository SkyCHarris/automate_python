
#? Step 1: Create a Regex for Phone Numbers

# First, we need to create a regex to search for phone numbers

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # separator
    \d{3}                       # first 3 digits
    (\s|-|\.)                   # separator
    \d{4}                       # last 4 digits
    (\s*(ext|x|ext.)\s*{2,5})?  # extension
)''', re.VERBOSE)

#TODO: Create email regex
#TODO: Find matches in clipboard text
#TODO: Copy results to the clipboard

# The TODO comments are just a skeleton for the program. They'll be replaced by code

# The phone number begins with an optional area code, so the area code group is followed with a question mark
# Since the area code can be just 3 digits (\d{3}) or 3 digits with parentheses (\(\d{3}\))...
    # ....we should have a pipe joining them
# We added the regex comment #Area code to help us remember what's supposed to match

# The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes
# The next few parts of the regex are straighforward:
    # 3 digits
    # Another separator
    # 4 digits
# Last part is optional:
    # Extension made up of any number of spaces followed by ext, x, or ext., followed by 2-5 digits


#? Step 2: Create a Regex for Email Addresses

# We will also need a regex that can match email addresses.

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-z0-9.-]+              # domain name
    (\.[a-zA-z]{2,4})           # dot something                    
)''', re.VERBOSE)

#TODO: Find matches in clipboard text
#TODO: Copy results to the clipboard

#* 1. The username part of the email address is one or more characters that can be any of:
    # lowercase and uppercase letters
    # numbers
    # a dot
    # an underscore
    # a percent sign
    # a plus sign
    # a hyphen
# These are all put into the character class in the brackets
#* 2. The domain and username are seprated by an @ symbol
#* 3. The domain name has a slightly less permissive character class with only:
    # letters
    # numbers
    # periods
    # hyphens
#* 4. The dot-com part (top-level domain) can really be dot-anything, but is between 2 and 4 characters

# This format for email addresses has weird rules
# This regex won't match every possible valid email address, but it'll match almost any typical email address encountered


#? Step 3: Find All Matches in the Clipboard Text

# Now that we have specified the regexes for phone numbers and email addresses...
    # we can let Python's re module do the hard work of finding all the matches on the clipboard

# The pyperclip.paste() function will get a string value of the text on the clipboard
# The findall() regex method will return a list of tuples

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)
for gropus in emailRegex.findall(text):
    matches.append(groups)

#TODO: Copy results to the clipboard

# There is one tuple for each match, and eatch tuple contains strings for each group in the regular expression
# Remember: group 0 matches the entire regex, so the group at index 0 of the tuple is the one you are interested in

#* 1. We store the matches in a list variable named 'matches'
    # It starts off as an empty list and a couple for loops
#* 3. For email addresses, we append group 0 of each match
#* 2. For the matched phone numbers, we don't want to just append group 0
    # Though the program detects phone numbers in several formats...
    # ...we want the phone number appended to be in a single, standard format
    # The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text
        # (area code, first 3 digits, last 4 digits, extension)


#? Step 4: Join the Matches into a String for the Clipboard

# Now we have email address and phone numbers as a list of strings in matches
# Let's put them on the clipboard
# The pyperclip.copy() function takes a single string value, not a list of strings, so we call the join() method on matches

# To make it easier to see that the program is working, let's print matches to the terminal
# If no phones or emails found, program should tell the user that

#! python3
# phoneandEmail.py - Finds phone numbers and email addresses on the clipboard

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')