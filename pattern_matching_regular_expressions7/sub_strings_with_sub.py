
#! Substituting Strings with the sub() Method

# Regular expressions can not only find text patterns, but also substitute new text in place of those patterns
# The sub() method for regex objects is passed two arguments
    # 1. First argument is a string to replace any matches
    # 2. Second argument is the string for the regular expression
# The sub() method returns a string with the substitutions applied

import re

namesRegex = re.compile(r'Agent \w+')

namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

# Sometimes you may need to use the matched text itself as part of the substitution
# In the first argument to sub(), you can type \1, \2, \3, and so on to mean "Enter the text of group 1, 2, 3 and so on, in the substitution"

# ex. Say you want to censor the names fo the secret agents by showing just the first letters of their names
# To do this you can use the:
    # regex Agent (\w)\w* and pass r'\1****' as the first argument to sub()
    # The \1 in that string will be replaced by whatever text was matched by group 1 - that is, the (\w) gropu of the regex

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
