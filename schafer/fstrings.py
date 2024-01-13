
#! F-Strings - How to Use Them and Advanced String Formatting

first_name = 'Sky'
last_name = 'Harris'

#* Format method

sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

#* f.string method

sentence = f'My name is {first_name} {last_name}'
print(sentence)
# add variables directly into placeholders
# more intuitively, can look at it directly

#* Run functions/methods directly in the f.string
# First/Last name capitalized

sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)

#* Print out Dictionary Values Using f.string

#* Format Method

person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

#* f.string Dictionaries

person = {'name': 'Jenn', 'age': 23}

sentence = f'My name is {person['name']} and I am {person['age']} years old'
print(sentence)

#* Calculations

calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)

#* More Advanced Formatting

for n in range(1, 11):
    sentence = f'The value is {n}'
    print(sentence)

# Let's 0 pad them by a certain amount

for n in range(1, 11):
    sentence = f'The value is {n:02}'   # Adds a 0 padding to the left of the num
    print(sentence)

# Ex. w/ Pi
# Extra formatting with :
    
pi = 3.14159265

sentence = f'Pi is equal to {pi:.4f}'   # .(decimal) 4 (# of digits) f (floating-point value)
print(sentence)

#* Formatting and Printing Dates

from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence = f'Jenn has a birthday on {birthday}'
print(sentence)
# would be nice if we could change to the format we like
# need to know datetime formatting codes

from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)