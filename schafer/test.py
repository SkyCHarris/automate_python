import os
os.chdir(r'C:\Users\slakk\OneDrive\Desktop\UETH - EDCON\Alex')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_underscore, file_number = file_name.split('DSF')
    
    new_name = f'{file_number}-{file_ext}'

    os.rename(f, new_name)