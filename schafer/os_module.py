
#! OS Module - Use Underlying Operating System Functionality

# Allows us to interact with underlying os:
# 1. Navigate file system
# 2. Get file info
# 3. Lookup and change env. variables
# 4. Move files around

import os

print(dir(os))

# Shows all the methods we have available

# Print current directory

import os

print(os.getcwd())

# Navigate to new location on file system

os.chdir(r'C:\Users\slakk\OneDrive\Desktop')

# See what files and folder are here in this directory (Desktop)
# Can pass a path, but dis betta

os.chdir(r'C:\Users\slakk\OneDrive\Desktop')

print(os.listdir())

# Create a new folder
# 2 diff. methods:
# 1. os.mkdir('') ->
# 2. os.mkdirs('') -> Create a directory that's a few levels deep? Creates intermediary directories

# 1. 
os.mkdir('OS-Demo-2')
# 2.
os.mkdirs('OS-Demo-2/Sub-Dir-1')

# Using only mkdirs makes it easy

# Delete folders
# 1. os.rmdir()
# 2. os.removedirs() -> Same as above

#1. 
os.rmdir('OS-Demo-2')

#2.
os.removedirs('OS-Demo-2/Sub-Dir-1')

# More dangerous to use removedirs, opt for rmdir

# Rename a file/folder

os.rename('test.txt', 'demo.txt')
# Original file name first, then name of new file

# Look at info about our files (print it)

print(os.stat('flow_control2'))

# More stats

# Size
print(os.stat('flow_control2').st_size)

# Modification time

print(os.stat('flow_control2').st_mtime)
# Returns timestamp
# To view in datetime format:

from datetime import datetime
import os

mod_time = os.stat('flow_control2').st_mtime
print(datetime.fromtimestamp(mod_time))
# Prints out human readable date and time

# See directory tree and files
# os.walk()
# Generated that yields tuple of 3 values as it walks dir. tree
# 1. Dir. path #2. Dir. in that path 3. Files w/in that path

from datetime import datetime
import os

for dirpath, dirname, filenames in os.walk(r'C:\Users\slakk\OneDrive\Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirname)
    print('Files:', filenames)

# Starts at Desktop as current path
# Prints all directories in desktop
# All files in Desktop
# Prints out directories one at a time
# All directories within subdirectories
# All files within subdirectories
# Keeps going until it's through the entire tree
    
# Say we have a file somewhere in our Desktop. Don't remember where it is
# Use os.walk() to find it
# Have WebApp? Need to keep track of file info in directory structure?
# Use os.walk() to collect file information
    
# Want to acess home directory location by grabbing home env. variable
    
print(os.environ) # All home env. variables
os.environ.get('OneDrive') # Choose one

# Use path to create a new file within home directory

'test.txt'
# Gotta figure out what path should be
# How do we combine path from environ.get + filename into a single file?

file_path = os.environ.get('OneDrive') + 'test.txt'
# Problematic. Slashes might be wonky

# Instead, use os.path module
# Lots of useful methods for working with paths
# Combines dir. w/ filename:

print(os.environ.get('OneDrive'))
file_path = os.path.join(os.environ.get('OneDrive'), + 'test.txt')
print(file_path)

# Create that file

with open(file_path, 'w') as f:
    f.wte

# More w/ os.path
    
# Grab filename of any path we're working on

print(os.path.basename('\\tmp\\test.txt'))

# Dir name of path

print(os.path.dirname('\\tmp\\test.txt'))

# Filename and dirname

print(os.path.split('\\tmp\\test.txt'))
# This was a fake path, let's check if one really exists

print(os.path.exists(''))

# splitext
# splits file root path and extension

print(os.path.splitext('\tmp\test.txt'))

# See all os.path modules

print(dir(os.path))

