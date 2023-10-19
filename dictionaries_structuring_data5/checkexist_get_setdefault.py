
#? Checking Whether a Key or Value exists in a Dictionary

# Recall that the in and not in operators can check whether a value exists in a list
# Use these operators to see whether a certain key or value exists in a dictionary

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
'Zophie' in spam.values()
'color' in spam.keys()
'color' not in spam.keys()
'color' in spam

# In this example, 'color' in spam is a shorter version of writing 'color' in spam.keys()
# This is always the case if you want to check whether a vlue is (or isn't) a key in the dictionary
    # usde the in (or not in) keyword with the dictionary value itself


#? The get() Method

# It's tedious to check whether a key exists in a dictionary before accessing that key's value
    # Dictionaries have a get() method that takes two arguments:
        # 1. The key of the value to retrieve
        # 2. A fallback value to return if that key does not exist

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

# Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method
# Without using get(), the code would have caused an error message

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing' + str(picnicItems['eggs'] + ' eggs')

#? The setdefault() Method

# You'll often have to set a value in a dictionary for a certain key if that key does not already have a value

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# The setfault() method offers a way to do this in one line of code
# The first argument passed to the method is the key to check for, and the secon argument is the value to set at that key if the key does not exist
    # If the key does exist, the setdefault() method returns the key's value

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam
spam.setdefault('color', 'white')
spam

# The first time setdefault() is called, the dictinoary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}
    # The method returns the value 'black' because this is now the value set for the key 'color'
# When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white' because spam already has a key named 'color'

# The setdefault() method is a nice shortcut to ensure that a key exists
# This short program counts the number of occurrences of eadh letter in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

# The program loops over each character in the message variable's string, counting how often each character appears
# The setdefault() method call ensures that the key is in the count dictionary ( with a default value of 0) so the program doesn't throw a KeyError error when count[character] = count[character] + 1 is executed
# This program works no matter what string is inside the message variable, even if the string is millions of characters long!git ad