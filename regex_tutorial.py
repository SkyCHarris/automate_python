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

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)




# Quantifiers: match more than 1 character at once
