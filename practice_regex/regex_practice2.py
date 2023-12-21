# Enter a regexp that matches all the items in the first column.
# You need to match the whole line, meaning a full match.

# rap them
# tapeth
# apth
# wrap/try
# sap tray
# 87ap9th
# apothecary

import re

word_digit_regex = re.compile(r'\w+\s?/?\w+')
word_digit_regex.findall('rap them, tapeth, apth, wrap/try, sap tray, 87ap9th, apothecary')
