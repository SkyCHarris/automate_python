
#! The Wildcard Character

# The . (or dot) character in a regex is called a wildcard and will match any character except for a newline

import re

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# Remember the dot character will match just one character, which is why the match for the text flat in the previous example only matched lat


#? Matching Everything with Dot-Star

# Sometimes you want to match everything and anything
    # ex. You want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and followed by anything again
# Use the dot-star (.*) to stand in for that "anything"
# Remember that the dot character means "any single character except the newline"
    # And the star character means "zero or more of the preceding character"

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)

# The dot-star uses greedy mode: it will always try to match as much text as possible
# To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?)
    # The question mark tells Python to match non-greedy
# See the difference between greedy and non-greedy:

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()


#? Matching Newlines with the Dot Charcter

# The dot-star will match everything except a newline
# By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# The regex noNewlineRegex, which did not have re.DOTALL passed to re.compile() call that created it, will match everything up to the first newline character
# The regex newlineRegex, which DID have re.DOTALL passed to re.compile(), matches everything

