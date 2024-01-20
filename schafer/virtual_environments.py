
#! VENV (Windows) - Use Virtual Environments with the Built-In venv Module

# Have a space to install packages for a specific project
# Each projects should have its own packages separate from each other

#* Create new virtual environment
# python3 -m venv project_env

#* Activate
# .\project_env\Scripts\activate.bat

#* Install packages for this venv
# request library -> pip install requests
# pytz -> pip install pytz

# (pip list shows packages)

#* Export these packages for a specific environment
# requirements.txt file
# pip freeze
    # Similar to pip list, but gives packages in correct form for requirements.txt file

#* Deactivate environment
# deactivate

#* Delete venv
# rmdir project_env /s (/s specifies even if not empty, still delete)

#* Create virtual environment
# Create inside of project
# Name it with venv (common convention)

# mkdir my_project
# python3 -m venv my_project\venv

#* Use requirements.txt file to create new venv with previous packages
# pip install -r
    # -r expects requirements.txt file

#* Common to put venv inside project folder, BUT, don't put project files inside venv
# Virtual environment should be something that can be thrown away and rebuilt
# so DON'T put project files in there

# Also, DON'T commit venv to source control
    # Can put in git.ignore
# requirements.txt can go in source control

#* Create environment with access to system packages
# pip list
    # These are the system packages installed on global version of python

    #* Create venv with access to these
    # python3 -m venv venv --system-site-packages
    # Puts all system packages inside this virtual environment
    # Additional packages we install won't affect global packages

#* List only the packages we've installed in this environment:
# pip list --local
# pip freeze --local