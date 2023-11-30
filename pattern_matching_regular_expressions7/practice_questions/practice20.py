# How would you write a regex that matches a number with commas for every three digits?
# Must match the following:

# '42'
# '1,234'
# '6,368,745'

import re

threeCommaRegex = re.compile(r'\d(,?|d\+)(,?\d+)')

threeCommaRegex.search('42')
threeCommaRegex.search('1,234')
threeCommaRegex.search('6,368,745')

# Actual:

import re

threeCommaRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

threeCommaRegex.search('42')
threeCommaRegex.search('1,234')
threeCommaRegex.search('6,368,745')
