
#? Step1

# Want to be able to run this program with a CLI argument that is a short key phrase- 'agree' or 'busy'
# The message associated with the key phrase will be copied to the clipboard so that the user can paste it into an email
# The user can then have long, detailed messages without need for retyping

#! python3
# mclip.py - A multi-clipboard program

TEXT = {
    'agree': "Yes, I agree. That sounds fine to me",
    'busy': "Sorry, can we do this later this week", 
    'upsell': "Would you consider making this a monthly donation?"
}

#? Step2

# Command line arguments will be stored in variable sys.argv
# First item in sys.argv list should be a string containing the program's filename (mclip.py)
# For this program, this argument is the key phrase of the message you want
# Since the command line argument is mandatory, display a usage message if the users forgets to add it (aka has less than 2 values in it)

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     # first command line arg is the keyphrase

#? Step3

# Now that the key phrase is stored as a string in the variable 'keyphrase', see whether it exists in the TEXT dictionary as a key
# If so, copy the key's value to the clipboard using pyperclip.copy()
    # (need to import pyperclip module)
# Note: You don't actually need the keyphrase variable, could just use sys.argv[1] everywhere keyphrase is used in the program
    # But a variable named keyphrase is more readable

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# This new code looks in TEXT dictionary for key phrase
    # If keyphrase is a key in dictionary, we get the value corresponding to that key, copy it to clipboard, and print message saying we copied
        # Else we print a message saying no keyphrase
# Now, using CLI and launching programs, easy/fast way to copy messages to clipboard
# Need to modify TEXT dictionary value in the source when you want to update the program with a new message

# In Windows you can create a batch file to run this program