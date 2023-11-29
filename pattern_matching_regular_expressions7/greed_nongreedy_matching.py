
#! Greedy and Non-Greedy Matching

# Since (Ha){3,5} can match 3, 4, or 5 instances of Ha in the string 'HaHaHaHaHa'...
    # ...you may wonder why the Match object's call to gropu() in the previous brace example returns 'HaHaHaHaHa' instead of the shorter possibilities
    # 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regex

# Python's regular expressions are 'greedy' by default
# In ambiguous situations they will mtach the longest string possible

# The 'non-greedy' (aka 'lazy') version ofthe braces, matching the shortest string possible, has the closing brace followed by a question mark

# Notice the difference between the greedy and non-greedy forms of the braces searching the same string:

import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

# The question mark can have two meanings in regular expressions:
    # 1. Declaring a non-greedy match
    # 2. Flagging an optional group