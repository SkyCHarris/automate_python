
#! The findall() Method

# In addition to the search() method, regex objects also have a findall() method
    # search() will return a Match object of the first matched text in the searched string
    # findall() will return the strings of every match in the searched string
# Let's see how search() returns a Match object only on the first instance of matching text:

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

# Alternatively, findall() will not return a Match object but a list of strings as long as there are no groups in the regex
# Each string in the list is a piece of the searched text that matched the regex

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-444-9999 Work: 212-555-0000')

# If there are groups in the regex, findall() will return a list of tuples
    # Each tuple represents a found match, and its items are the matched strings for each group in the regex
# To see findall() in action, notice that the regex being compiled now has groups in parentheses:

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-444-9999 Work: 212-555-0000')

# To summarize what the findall() method returns:

# 1. When called on a regex with no gropus, the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000']
# 2. When called on a regex that has groups, the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')]
