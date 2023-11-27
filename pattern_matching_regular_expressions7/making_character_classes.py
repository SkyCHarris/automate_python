
#! Making Your Own Character Classes

# There are times you want to match a set of characters, but the shorthand character classes are too broad
# Define your own character class using square brackets
    # ex. The character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

# You can also include ranges of letters or numbers by using a hyphen
    # ex. The character class [a-zA-Z0-9] will match all lowercase leters, uppercase letters, and numbers

# Note that inside the square brackets, the normal regex symbols are not interpreted as such
# You do not need to escape the ., *, ?, or () characters with a backslash
    # ex. The character class [0-5.] will match digits 0 to 5 and a period

# By placing a caret character (^) just after the character's opening bracket, you can make a negative character class
    # A negative character class will match all the characters that are NOT in the character class

import re

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

# Now, instead of matching every vowel, we're matching every character that isn't a vowel

