
#! Read, Parse, and Write CSV Files

# CSV -> Comma Separated Values
# Allow us to put into plain text file some data
    # Use delimeter to separate fields (usually comma)

# Top line has our fields:
    # first_name
    # last_name
    # email

# vs split()
# CSV module handles random inputs, newlines, etc. with ease

import csv

# read csv file
with open('names.csv', 'r') as csv_file: # 'r' = read
    csv_reader = csv.reader(csv_file)   # by default expects values to be sep. by commas
# csv_reader needs to be iterated over
    for line in csv_reader:
        print(line)

# Print out specified index values:

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])

# Skip first line (category)
# next()
        
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)    # skips over first line

    for line in csv_reader:
        print(line[2])

# Write to a csv file
# Save same values to new file, but use - instead of , as delimeter

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')   # writes to new file, 2nd argument is delimeter
        
        # write each line of old file into new file
        for line in csv_reader:
            csv_writer.writerow(line)   

# Read in the tab delimited file

with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
# didn't read the file properly, each line has one value, didn't split on tab bc was expecting comma
        
# Pass in '\t' delimiter
        
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

# Dictionary Reader / Dictionary Writer
# Dict.Reader()
        
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
# print out is now an ordered dictionary
# doesn't include field names, starts with the first person value
# field names are now the keys of each of these values
        
# Get values based on keys:
        
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])
# gives only the email info for each entry/row
        
# Dict.Writer
# (need to specify field names)
# (have option to write out fieldnames or not) -> .writeheader()
        
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']   # field names specified
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')   # pass in field names variable here

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

# Want first and last name, but leave off email
# Would need to use index if using simply .reader/.writer
            
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']   
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)