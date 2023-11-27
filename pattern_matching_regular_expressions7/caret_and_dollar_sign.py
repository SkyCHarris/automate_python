
#! The Caret and Dollar Sign Characters

# You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched tex
# You can use a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern
# Use the ^ and $ together to indicate that the entire string must match the regex- that is, it's not enough for a match to be made on some subset of the string

# ex. r'^Hello' regex string matches strings that begin with 'Hello'

import re

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
beginsWithHello.search('He said hello.') == None

# The r'\d$ regular expression string matches strings that end with a numeric character from 0 to 9

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None

# The r'%\d+$ regex string matches strings that both begin and end with one or more numeric charcters

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12 34567890') == None

# The last 2 search() calls demonstrate hoe the entire string must match the regex if ^ and $ are used
# Use the mnemonic "Carrots cost dollars" to remind yourself that the caret comes first and dollar sign comes last