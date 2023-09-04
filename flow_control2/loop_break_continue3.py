# while Loop Statements

# -Make a block of code execute over and over again using a while statement
# -The code in a while clause will be executed as long as the while statement's condition is True.
# -A while statement always consists of:
# 1. The while keyword
# 2. A condition (an expression that evaluates to True or False)
# 3. A colon
# 4. Starting on the next line, an indented block of code (the while clause)

# -At the end of a while clause, the program execution jumps back to the start of the while statement (unlike an if clause which continues after the if statement)


# if statement
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

# while statement
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# -In the while loop, the condition is always checked at the start of each iteration (each time the loop is executed). 
# -If true, the clause is executed, and afterwards the condition is checked again

# An Annoying While Loop

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# break Statements

# -There's a shortcut to get the program execution to break out of a while loop's clause early
# -If execution reaches a break statement, it immediately exits the while loop's clause

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue Statements

# -Like break statements, continue statements are used inside loops
# -When the program execution reaches a continue statement, the program execution jumps back to the start of the loop and reevaluates the loop's condition
#   -This is also what happens when the execution reaches the end of the loop

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# Truthy and Falsey Values

# -Conditions consider some values in other data types equivalent to True and False
# -0, 0.0, and '' considered False in conditions. All other values considered True

name = ''
while not name:
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
        print('Be sure to have enough room for all your guests.')
print('Done')


# for Loops and the range() Function

# -What if you want to execute a block of code only a certain number of imtes?
# -Do so using for loop statements and the range() function
# -A for statement looks something like 'for i in range(5), and includes:
# 1. The for keyword
# 2. A variable name
# 3. The in keyword
# 4. A call tot he range() method with up to three integers passed to it
# 5. A colon
# 6. Starting on the next line, an indented block of code (the for clause)

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# -The variable i will go up to, but will not include, the integer passed to range()
# -Continue and Break statements can only be used inside for loops

total = 0
for num in range(101):
    total = total + num
print(total)

# An Equivalent while loop

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# The Starting, Stopping, and Stepping Argumnets to range()

# -Some functions can be called with multiple arguments separated by a comma. range() is one of them
# -This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero

for i in range(12, 16):
    print(i)

# -range() function can also be called with three arguments.
# -First two arguments are start and stop values, third will be the step argument (integer at which it 'steps')

for i in range(0, 10, 2):
    print(i)

# -range() function is flexible in the sequence of numbers it produces for 'for loops'
# -You can make the step argument a negative number to make the for loop count down instead of up

for i in range(5, -1, -1):
    print(i)