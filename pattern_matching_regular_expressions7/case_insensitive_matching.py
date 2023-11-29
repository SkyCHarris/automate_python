
#! Case-Insensitive Matching

# Normally regexes match text with the exact casing you specify. Ex.

import re

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

# But sometimes you only care about matching the letters without worrying about case sensitivity
# Pass re.IGNORECASE or re.I as a second argument to re.compile()

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

robocop.search('ROBOCOP protects the innocent.').group()

robocop.search('Al, why does your programming book talk about robocop so much?').group()