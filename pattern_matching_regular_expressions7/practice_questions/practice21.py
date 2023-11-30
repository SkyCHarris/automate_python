# How would you write a regex that matches the full name of someone whose last name is Watanabe?
# Assume that the first name that comes before it will always be one word that begins with a capital letter

# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'

import re

watanabeRegex = re.compile(r'[A-Z]+[Watanabe]')

watanabeRegex.search('Haruto Watanabe')
watanabeRegex.search('Alice Watanabe')
watanabeRegex.search('RoboCop Watanabe')

watanabeRegex.search('haruto Watanabe')
watanabeRegex.search('Mr. Watanabe')
watanabeRegex.search('Watanabe')
watanabeRegex.search('Haruto watanabe')

# Attempt 2

import re

watanabeRegex = re.compile(r'[A-Z]+\s*[Watanabe]')

mo1 = watanabeRegex.search('Haruto Watanabe')
mo2 = watanabeRegex.search('Alice Watanabe')
mo3 = watanabeRegex.search('RoboCop Watanabe')

mo4 = watanabeRegex.search('haruto Watanabe')
mo5 = watanabeRegex.search('Mr. Watanabe')
mo6 = watanabeRegex.search('Watanabe')
mo7 = watanabeRegex.search('Haruto watanabe')

mo1.group()
mo2.group()
mo3.group()
mo4.group()
mo5.group()
mo6.group()
mo7.group()

# Attempt 3

import re

watanabeRegex = re.compile(r'[A-Z]\w+\s[A-Z]\w+')

mo1 = watanabeRegex.search('Haruto Watanabe')
mo2 = watanabeRegex.search('Alice Watanabe')
mo3 = watanabeRegex.search('RoboCop Watanabe')

mo4 = watanabeRegex.search('haruto Watanabe')
mo5 = watanabeRegex.search('Mr. Watanabe')
mo6 = watanabeRegex.search('Watanabe')
mo7 = watanabeRegex.search('Haruto watanabe')

mo1.group()
mo2.group()
mo3.group()
mo4.group()
mo5.group()
mo6.group()
mo7.group()

# Actual

import re

watanabeRegex = re.compile(r'[A-Z][a-z]*\sWatanabe')

mo1 = watanabeRegex.search('Haruto Watanabe')
mo2 = watanabeRegex.search('Alice Watanabe')
mo3 = watanabeRegex.search('RoboCop Watanabe')

mo4 = watanabeRegex.search('haruto Watanabe')
mo5 = watanabeRegex.search('Mr. Watanabe')
mo6 = watanabeRegex.search('Watanabe')
mo7 = watanabeRegex.search('Haruto watanabe')

mo1.group()
mo2.group()
mo3.group()
mo4.group()
mo5.group()
mo6.group()
mo7.group()