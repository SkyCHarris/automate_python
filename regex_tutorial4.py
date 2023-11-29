import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ % * + { } [ ] \ | ( )

stimdy.com

435-393-5526
433.388.2343
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)

# .finditer ->  Returns match objects with extra information and functionality
# .findall  ->  Return matches as a list of strings. 
#                   -If matching groups, will only return the groups
#                   -If multiple groups, will return a list of tuples containing all of the groups
#                   -If there are no groups, just returns all of the matches in a list of strings
# .match    ->  Find matche at the beginning of the string
# .search   ->  Search for matches within the entire string


# Flags: matches uppercase/lowercase
    # ex. re.IGNORECASE / re.I
    # ex. re.multiline
    # ex. re.verbose