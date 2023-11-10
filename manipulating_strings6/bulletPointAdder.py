
#! Project: Adding Bullets to Wiki Markup

# When editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a star in front
# But say you have a large list that you want to add bullet points to
# You could just type those stars at the beginning of each line, one by one, or:
    # You could automate this task with a short Python script

# This script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard

Lists of animals
Lists of aquarium life
Lists of bioligists by author abbreviation
Lists of cultivars


#? Step 1: Copy and Paste from the Clipboard

# 1. Paste text from the clipboard
# 2. Do something to it
# 3. Copy the new text to the clipboard

# Second step is a little tricky, but steps 1 and 3 are pretty straightforward: pyperclip.copy() and pyperclip.paste()
# Let's do those first



#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars

pyperclip.copy(text)


#? Step 2: Separate the LInes of Text and Add the Star

# The call to pyperclip.paste() returns all the text on the clipboard as one big string
# If we used the "List of Lists of Lists" example, the strings tored in text would look like this:

#* 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

# We could write code that searches for each \n newline character in the string then adds a star just after that
    # But it's easier to use the split() method to return a list of strings, one for each line in the original string, and then add the start to the front of each string in the list


import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # add star to each string in 'lines' list

pyperclip.copy(text)

# We split the text along its newlines to get a list in which each item is one line of the text
# We store the list in lines and then loop through the items in lines
# For each line, we add a star and a space to the start of the line
# Now, each string in lines begins with a star


#? Step 3: Join the Modified Lines

# The lines list now contains modified lines that start with stars
    # But pyperclip.copy() is expecting a single string value, not a list of string values
# To make this a single string value, pass lines into the join() method to get a single string joined from the list's strings

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # add star to each string in 'lines' list
text = '\n'.join(lines)

pyperclip.copy(text)

# When this program is run, it replaces the text on the cliboard with text that has stars at the start of each line
    # Now the program is complete, and you can try running it with text copied to the clipboard

* Lists of animals
* Lists of aquarium life
* Lists of bioligists by author abbreviation
* Lists of cultivars
*

* Lists of animals
* Lists of aquarium life
* Lists of bioligists by author abbreviation
* Lists of cultivars