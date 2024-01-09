
#! Dictionaries

# Work with key value pairs (hashmaps, associative arrays)
# Key: unique identifier where we can find our data
# Value: the data

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# Let's get value of just one key
# Add [] after dictionary, specify key

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['courses'])

# Values can be just about any datatype
# Keys can be any immutable datatype

student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student[1])

# What if we access a key that doesn't exist?

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['phone'])

# Throwing an error might not be what we want
# We may just want to return None or a default value
#* Get method

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('phone'))
# >>> None

# Specify default value for keys that don't exist

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('phone', 'Not Found'))

# Add new entry to dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'

print(student.get('phone', 'Not Found'))

# If a key already exists, we set value like this, it'll update that key

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)

# Can also update values using the update method
# Useful when updating mult. values at a time
# Takes in dictionary as an argument

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print(student)

# Delete a specific key and its value
# del

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

del student['age']

print(student)

# Pop removes, and returns
# Can grab that removed value with a variable

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

age = student.pop('age')

print(student)
print(age)

# Loop through all keys and values of dict.
# Check # of keys by printing len()

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(len(student))

# See keys

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.keys())

# See values

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.values())

# See keys and values

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.items())

# Loop through
# If we loop without method, just loops through keys

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)