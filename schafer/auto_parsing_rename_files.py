
#! Automate Parsing and Renaming of Multiple Files

import os   # Navigate files system, change file names, etc.
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

print(os.getcwd())

for f in os.listdir():
    print(f)
# print list of file names
    
# Remove extension
    
import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    print(os.path.splittext(f))
# splits off extension
    
import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
# sets variables for name and extension
    
# Rename file so numbers are at the beginning
    
import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('DSF'))

# Create new variables to capture split
    
import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_underscore, file_number = file_name.split('DSF')
    print(file_number)

# Print formatted string in a way we want file to be represented
    
import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_underscore, file_number = file_name.split('DSF')
    print(f'{file_number}-{file_ext}')

# Rename

import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_underscore, file_number = file_name.split('DSF')
    
    new_name = f'{file_number}-{file_ext}'

    os.rename(f, new_name)
