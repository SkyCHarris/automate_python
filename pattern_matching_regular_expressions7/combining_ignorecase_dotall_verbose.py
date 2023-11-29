
#! Combining re.IGNORECASE, re.DOTALL, re.VERBOSE

# What if you want to use re.VERBOSE to write comments in your regex, but also want to use re.IGNORECASE to ignore capitalization?
# Unfortunately, re.compile() function only takes a single value as its second argument
# Get around this limitation by combining these 3 variables using the pipe character |, aka the bitwise operator

# So if you want a regex that's case-insensitive AND includes newlines to match the dot character, form your re.compile() call like this:

import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

# All three options:

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# This syntax is a little old-fashioned and originates from early versions of Python
# The details of the bitwise operator are beyond the scope of this book

