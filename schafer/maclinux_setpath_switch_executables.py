
#! How to Set the Path and Switch Between Different Versions/Executables (Mac & Linux)

#* Find file path

# which python3
# /c/Users/slakk/AppData/Local/Programs/Python/Python312/python3

# type python3
# python3 is hashed (/c/Users/slakk/AppData/Local/Programs/Python/Python312/python3)

#* echo $PATH
# Directories where my machine is looking for commands
# /c/Users/slakk/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/slakk/bin:/c/Windows/system32:/c/Windows:/c/Windows/System32/Wbem:/c/Windows/System32/WindowsPowerShell/v1.0:/c/Windows/System32/OpenSSH:/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files/dotnet:/cmd:/c/Users/slakk/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/slakk/AppData/Local/Programs/Python/Python312:/c/Users/slakk/AppData/Local/Microsoft/WindowsApps:/c/Users/slakk/AppData/Local/Programs/Microsoft VS Code/bin:/c/Users/username/Anaconda3:/usr/bin/vendor_perl:/usr/bin/core_perl

# If it finds a different bin than you wanted, you'll have issues

#* Run Anaconda Version of Python
# "C:\Users\slakk\anaconda3\python.exe"

# Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

# Not on path

#* Add Anaconda Directory to our Path
# nano .bash_profile
# PATH="C:\Users\slakk\anaconda3:${PATH}"
    # Adds current value of the path to the end of this string
# export PATH
    # Set path to this new variable

# echo $PATH
# C:\Users\slakk\anaconda3:/c/Users/slakk/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/slakk/bin:/c/Windows/system32:/c/Windows:/c/Windows/System32/Wbem:/c/Windows/System32/WindowsPowerShell/v1.0:/c/Windows/System32/OpenSSH:/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files/dotnet:/cmd:/c/Users/slakk/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/slakk/AppData/Local/Programs/Python/Python312:/c/Users/slakk/AppData/Local/Programs/Microsoft VS Code/bin:/c/Users/username/Anaconda3:/c/Program Files (x86)/python312:/c/Users/slakk/AppData/Local/Microsoft/WindowsApps:/usr/bin/vendor_perl:/usr/bin/core_perl

#* Create an alias
# alias python=python3

# Alias will go away when we restart terminal
# To make permanent, add to bash_profile
# nano .bash_profile (need to be in home directory)
# alias python=python3
# alias pip=pip3
    # Ctrl-x -> y -> Enter

#* Check all pip installations (?)
# pip list

#* Python Working, but No Idea Path or Which Executable
# python3
# import sys
# sys.executable

# Troubleshoot why running one python and not other:
# echo $PATH