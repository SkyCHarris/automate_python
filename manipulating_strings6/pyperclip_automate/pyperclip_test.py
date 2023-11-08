
#! Copying and Pasting Strings with the pyperclip Module

# The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer's clipboard
# Sending the output of your program to the clipboard will make it easy to paste it into an email, word processor, or some other software
# The pyperclip module does not come with Python, to install it follow the directions in Appendix A

import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()

#TODO: Should create a virtual environment to do this
#TODO: Create virtual environment in VSCode terminal: python -m venv (my environment name)
#TODO: Virtual environment is now created, but needs to be activated: myenv -> bin -> run activate file
    #TODO: myenv\bin\activate (in VSCode terminal)
    #TODO: permission denied fix -> (terminal) chmod +x myenv/bin/activate

import pyperclip
pyperclip.copy('Hello, world! This is a test for the pyperclip module to copy to clipboard from a python program')
pyperclip.paste()