
#! Character Classes

# In the earlier phone number regex example we learned that \d could stand for any numeric digit
    # That is, \d is shorthand for the regex (0|1|2|3|4|5|6|7|8|9).
# There are many such shorthand character classes:

#* \d       Any numeric digit from 0 to 9
#* \D       Any character that is NOT a numeric digit from 0 to 9
#* \w       Any letter, numeric digit, or the underscore character (think of this as matching "word" characters)
#* \W       Any character that is NOT a letter, numeric digit, or the underscore character
#* \s       Any space, tab, or newline character (think of this as matching "space" characters)
#* \S       Any character that is NOT a space, tab, or newline

# Character classes are nice for shortening regular expressions
# The character class [0-5] will match only the numbers 0 to 5; much shorter than typing (0|1|2|3|4|5)
# Note that while \d matches digits and \w matches digits, letters, and the underscore, there is no shorthand character class that matches only letters
    # (Though you can use the [a-zA-Z] character class explained next)

import re

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# The regex \d+\s\w+ will match text that has:
    # 1. One or more numeric digits (\d+) 
    # 2. Followed by a whitespace character (\s)
    # 3. Followed by one or more letter/digit/underscore characters (\w+)

# The findall() method returns all matching strings of the regex pattern in a list

