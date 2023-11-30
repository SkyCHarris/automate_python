# Can pass through a function without doing much, but not throwing errors:

def hello_func():
    pass        # Pass through a function without doing much, but not throwing errors:

hello_func() # function call


# Practice 1
def hello_func():
    print('Hello Function')

hello_func()

# Return: allows us to operate on data, then pass the result to whatever called our function
    # When we execute our function, it will be equal to our return value

def hello_func():
    return 'Hello Function.'

print(hello_func())

# Think of a function as a machine that takes input and produces a result
# Functions are like a black box:
    # You don't need to think much about what it's doing, just concern yourself with input/output

print(len('Test'))

# Looking at functions in this way let's you treat the return value just like the data type that it is

# Chaining methods:

def hello_func():
    return 'Hello Function.'

print(hello_func().upper)

# Passing arguments

def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))

# Need to pass in greeting argument when we call our function
# Greeting parameter is a required argument- has no default value
    # Let's try: ('You' is the default value)

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', 'James'))

# Some functions in Python like this (tricky):

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# Allows us to accept an arbitrary number of positional or keyword arguments
    # ex. Let's say student_info function takes positional arguments that represent:
        # 1. Classes that student is taking
        # 2. Random information about the 
# Names don't have to be args and kwargs!

# Let's call the function with some random values

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name ='John', age=22)

# When we printed args, it's actually a tuple with all of our positional arguments
# Our kwargs are a dictionary with all of our keyword values

# May see a function call with arguments using * or **
    # When used in this context, it unpacks a sequence or dictionary and passes those values into the function individually

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)

# Let's say we wanna pass all of these courses in as our positional arguments
    # and info dictionary as our keyword arguments
# This ain't what we want

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)

# Instead of passing in values individually, we placed complete list and complete dicitonary as positional arguments
# BUT if we use * in front of our list, and ** in front of our dictionary, it will unpack the values and put them in individually

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)