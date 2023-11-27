
#! More Pattern Matching with Regular Expressions

# Time to try some more powerful pattern-matching capabilities!

#? Grouping with Parentheses

# Say you want to separate the area code from the rest of the phone number
# Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d)
# Then you can use group() match object method to grab the matching text from just one group

# The first set of parentheses in a regex string will be group 1
    # The second will be group 2
# By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text
# Passing 0 or nothing to the group() mtehod will return the entire matched text

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()

# If you'd like to retrieve all the groups at once, use the groups() method (note the plural form)

mo.groups()
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# Since mo.groups() returns a tuple of multiple values, you can use the multiple-assignment trick to assign each value to a separate value

# Parentheses have a special meaning in regular expressions. But what to do if you need to match a parenthesis in your text?
    # Need to escape these characters with a backslash \

import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
mo.group(2)

# The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters
# In regexes, the following characters have special meanings:
    # . ^ $ * + ? { } [ ] \ | ( )

# To detect them as part of your text pattern, escape them with a backslash:
    # \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)


#? Matching Multiple Groups with the Pipe

# The | character is called a pipe
# Use it anywhere you want to match one of many expressions
    # ex. the regex r'Batman | Tina Fey' will match either 'Batman' or 'Tina Fey'
# When both Batman and Tina Fey occur in the searched string, the first occurence of matching text will be returned as the Match object

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

# You can find all matching occurrences with the findall() method

# You can also use pipe to match one of several patterns as part of your regex
    # ex. You want to match any of the strings 'Batman', 'Batmobile', 'Batcopter', 'Batbat'. 
# Since all these strings start with Bat, would be nice to specify this prefix just once
# Do this with parentheses:

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

# The method call mo.group() returns the full matched text 'Batmobile', while mo.group(1) returns just the part of the matched text inside the first parentheses group 'mobile'
# By using the pipe character and grouping parentheses, you can specify several alternative patterns you would like your regex to match


#? Optional Matching with the Question Mark

# Sometimes there's a pattern you want to match only optionally
    # That is, the regex should find a match regardless of whether that bit of text is there
# The ? character flags the group that precedes it as an optional part of the patter

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

# The (wo)? part of the regex means that the pattern wo is an optional group
# The regex will match text that has zero instances or one instance of wo in it
    # That's why the regex matches both 'Batwoman' and 'Batman'
# Using the eariler phone number example, you can make the regex look for phone numbers that do or do not have an area code

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()

# You can think of the ? as saying: "Match zero or one of the group preceding this question mark"