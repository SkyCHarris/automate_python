
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


#? Matching Zero or More with the Star

# The * (called star or asterisk) means "match zero or more"
    # - The group that precedes the star can occur any number of times in the text
    # It can be completely absent or repeated over and over again

import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search("The Adventures of Batwoman")
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

# For 'Batman', the (wo)* part of the regex matches zero instances of wo in the string
# For 'Batwoman', the (wo)* matches one instance of wo
# For 'Batwowowowoman', (wo)* matches four instances of wo

# If you need to match an actual star character, prefix the star in the regex with a backslash \*


#? Matching One or More with the Plus

# While * means "match zero or more", the + (plus) means "match one or more".
# Unlike the star, which doesn't require its group to appear in the matched string, the group preceding a plus must appear at least once

import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

# The regex Bat(wo)+man will not match the string 'The Adventures of Batman' because at least one wo is required by the + sign


#? Matching Specific Repetitions with Braces

# If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in braces
    # ex. The regex (Ha){3} will match the string 'HaHaHa', but will not match 'HaHa'
# Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum
    # ex. The regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'
# You can also leave out the first or second number in the braces to leave the min or max unbounded
    # ex. (Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances
# Braces can help make your regexes shorter

# These two regexes match identical patterns:

#* (Ha){3}
#* (Ha)(Ha)(Ha)

# These two regexes also match identical patterns:

#* (Ha){3,5}
#* ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
mo2 == None