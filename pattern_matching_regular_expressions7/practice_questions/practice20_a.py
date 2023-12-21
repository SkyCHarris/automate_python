# How would you write a regex that matches a number with commas for every three digits?

# '42'
#'1,234'
#'6,368,745'

# NOT

# '12,34,567'
# '1234'

import re

three_comma = re.compile(r'\d{1,3}(,\d{3})*')
mo = three_comma.search('42')
mo2 = three_comma.search('1,234')
mo3 = three_comma.search('6,368,745')
mo.group()
mo2.group()
mo3.group()