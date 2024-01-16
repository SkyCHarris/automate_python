
#! Real World Example - Parsing Names from a CSV to an HTML List

# First row is headers:
# FirstName,LastName,Email,Pledge, etc.

# People values start on line 5
# Line 35 is the cut off for people saying they want to be listed for rewards

import csv

html_output = ''    # end goal is to have html version
names = []  # will want to capture all the names

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(csv_data)

# Returns an object that's an iterable and behaves like a generator
# To get our desired result we need to either:
    # 1. Loop over it to get each line
    # 2. Convert to a list

import csv

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    
    print(list(csv_data))   # converted to list
# prints out a bunch of data, not easy to read
    
# Print line for line
    
html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)
# more readable than list
        
# Step over values in an iterable:
# next()
        
html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)  # skip over line
    next(csv_data)  # skip over line

    for line in csv_data:
        print(line)

# Add each name to list of names

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)  # skip over line
    next(csv_data)  # skip over line

    for line in csv_data:
        names.append(f'{line[0]} {line[1]}')

for name in names:  # hmmmm...
    print(name)

# Every name after 'No Reward Description' line shouldn't be added
# Add in a check for that line
    # break out of loop when we see that value

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)  # skip over line
    next(csv_data)  # skip over line

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

for name in names:
    print(name)

# Get names into an html unordered list to drop into patreon site
# Add # of supporters

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)  # skip over line
    next(csv_data)  # skip over line

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

print(html_output)

# Unordered List

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)  # skip over line
    next(csv_data)  # skip over line

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

# Dict.Reader()

html_output = ''
names = [] 

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
