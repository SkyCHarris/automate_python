# Storing Values in Variables

# -A 'variable' is like a box in the computer's memory where you can store a single value
# -If you want to use the result of an evaluated expression later in your program, you can save it inside a variable

# Assignment Statements

# -Store values in variables using an 'assignment statement'
# -Consists of: variable name, equal sign (assignment operator), and value to be stored

spam = 40
print(spam)

eggs = 2
print(spam + eggs)

print(spam + eggs + spam)

spam = spam + 2
print(spam)

# -A variable is 'initialized' (created) the first time a value is stored in it
# 1. Variable can then be used in an expression
# 2. When a variable is assigned to a new value...
# 3. The old value is forgotten
# -This is called 'overwriting' the variable

spam = 'Hello'
print(spam)

spam = 'Goodbye'
print(spam)

# Variable Names

# -A good variable name describes the data it contains
# Rules:
# +It can be only one word with no spaces
# +It can use only letters, numbers, and the underscore _ character
# +It can't begin with a number