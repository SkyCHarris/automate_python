
#! Managing Complex Regexes

import re

# Regexes are fine if the text pattern you need to match is simple
# But matching complicated text patterns might require long, convoluted regular expressions
# Mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regex string
# This 'verbose mode' can be enabled by passing the variable re.VERBOSE as the 2nd argument to re.compile()

# Instead of:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*{2,5})?)')

# You can spread the regex over multiple lines with comments like:

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # separator
    \d{3}                       # first 3 digits
    (\s|-|\.)                   # separator
    \d{4}                       # last 4 digits
    (\s*(ext|x|ext.)\s*{2,5})?  # extension
)''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax (''') to create a multiline string
    # so you can spread the regex definition over multiple lines, more legible
# The comment rules inside the regex string are the same as regular Python code
    # the # symbol and everything after it are ignored (comment)
    # extra spaces inside the multiline string for the regex are not considered part of the text pattern to be matched

