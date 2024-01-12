
#! How to Set the Path and Switch Between Different Versions/Executables (Windows)

#* Tried installing Python. Still not working?

# Grab path from File Explorer
# ex. "C:\Program Files (x86)\python312\python.exe.exe"
    # This threw an error because of the (x86)
    # Need to avoid it or fix all my file names yikes

# System -> Advanced Settings -> Environment Variables
    # New
    # Edit
    # Move up/down (Will decide priority on which Python files are executed first)

# Python now gives you the option to auto-add installation directory to the path automatically

# Add pip to the path
# Not in the same directory as python
# Inside the 'Scripts' directory
    # NOT for me
    # pip 23.3.2 from C:\Users\slakk\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

#* Python command working, but not sure which executable you're looking or where it's located?

# See exactly which Python installation we're running:
# import sys
# sys.executable
# 'C:\\Users\\slakk\\AppData\\Local\\Programs\\Python\\Python312\\python3.exe'

# Is this the path we we're looking for?
# Yes? -> Great
# No? -> See below
    # Check path environment variable again
    # Move env variables up/down in System -> Advanced Settings

# To view entire path from within command line:
# (supposedly) echo %PATH% (but not working for me)

#* Pip installed modules not working? Not importing?
# Can also be a path issue
# Check details with:
    # pip show (module)
    # ex. pip show django

# Make sure location of that package is in same directory (site-packages for me)
# C:\Users\slakk\AppData\Local\Programs\Python\Python312\Lib\site-packages

#* Command Line using correct version of python, editor isn't
# Compare sys.executable value with editor's 'build systems' (sublime text)

# What if you wanna use diff version of python, or the env from a venv?

#* Virtual Environments
# Have separate python environment per project
    # Executables, packages, etc.
# Cmd line helps
# Code includes that adds and removes directories to beginning of path for you


