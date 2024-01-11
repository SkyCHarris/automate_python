
#! Reading and Writing Files

# Will interact with files a lot

# Get a file object
# open

# This is normally not the recommended way

# File Objects

f = open('test2.txt')
# specify reading, writing, appending, or reading+writing
# 'r', 'w', 'a', 'r+' 

f = open('test2.txt', 'r')

print(f.name)   # print name of file

f.close()
# need to also close file
# if not, get leaks and errors in applications

# Context Manager (preferred)

with open('test2.txt', 'r') as f:   # f is the variable name
    pass
    # file automatically closes after exiting this block of code

print(f.name)

# Read contents from file here within context manager

with open('test2.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# What if we have a large file, but don't want to load all the contents
    
with open('test2.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)
# gives list of all the lines in the file

# Get first line
    
with open('test2.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
# every time we run it we get the next line in our file
    
# Iterate over the lines in a file
    
with open('test2.txt', 'r') as f:

    for line in f:
        print(line, end='')
# doesn't read in file contents all at once
        
# More control:
# Specify amount of data you want to read
    # Pass in size as argument
        
with open('test2.txt', 'r') as f:
    f_contents = f.read(20)    # num. of characters
    print(f_contents)

# Can be done in mult. iterations
    
with open('test2.txt', 'r') as f:
    f_contents = f.read(20)
    print(f_contents, end='')

    f_contents = f.read(20)
    print(f_contents, end='')

# How to use this technique to read in a large file
# Use a loop to iterate over chunks at a time
    
with open('test2.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)   # kicks back out to while loop, checks if we hit end of file, f.read will return empty string and not hit > 0 conditional
# when reading from files we see that it advances its position every time
        
# Use f.tell to see current position
        
with open('test2.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
    # says we're currently at the 10th character position in the file

# Manipulate current position with f.seek
    
with open('test2.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)

# We want second f.read() to start back at the beginning of the file
# f.seek()
    
with open('test2.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)
    # comes back to the beginning, but can be placed anywhere in the file

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)

# What if we try to write from a file we have open in read mode?
    
with open('test2.txt', 'r') as f:
    f.write('Test')
    # throws an error

# Write to a file
# If the file doesn't exist already, this will create it
# If it does exist, it'll overwrite it

with open('test3.txt', 'w') as f:
    pass

# To write to this file, use f.write()

with open('test3.txt', 'w') as f:
    f.write('Test')

# If we do another write, it'll pick up where we left off (just like f.read())

with open('test3.txt', 'w') as f:
    f.write('Test')
    f.write('Test')

# Use f.seek() to set position back to the beginning of the file
    
with open('test3.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Test')

# Let's pull it all together!
# Make a copy of test2.txt file
    
with open('test2.txt', 'r') as rf:  # rf = 'readfile'
    with open('test_copy.txt', 'w') as wf:  # wf = 'writefile'
        for line in rf:
            wf.write(line)

# Copy a large picture file using file objects
# Need to use binary mode!
            
with open('zaradesk.jpg', 'rb') as rf:  # rf = 'readfile'
    with open('zaradesk_copy.jpg', 'wb') as wf:  # wf = 'writefile'
        for line in rf:
            wf.write(line)

# More control over exactly what you're reading and writing

with open('zaradesk.jpg', 'rb') as rf:
    with open('zaradesk_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)