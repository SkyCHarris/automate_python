# Functions

# -A function is like a miniprogram within a program

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

# 1. First line is a def statement which defines a function named hello()
# 2. The code that follows is the body of the function. It is executed when the function is called, not when it's defined.
# 3. The hello() lines after the function are function calls

# -A major purpose of functions is to group code that gets executed multiple times
# -Avoid duplicating code

# _______________


# def Statements with Parameters

# -When  you call the print() or len() functions, you pass them values called 'arguments' by typing them between the parentheses.
# -You can also define your own functions that accept arguments

def hello(name):
    print('Hello, ' + name)

hello('Alice')
hello('Bob')

# -The definition of the hello() function in this program has a parameter called 'name'
# 1. Parameters are variables that contain arguments. When a function is called with arguments, the argumnets are stored in the parameters
# 2. When a function is called with arguments, the argumnets are stored in the parameters
# 3. The program execution enters the function, and the parameter 'name'' is automatically set to 'Alice', which gets printed by print() statement

# Note: The value stored in a parameter is forgotten when the function returns


# Define, Call, Pass, Argument, Parameter

def sayHello(name):
    print('Hello, ' + name)
sayHello('Al')

# -To define a function is to create it, just like an assignment statement like spam = 42 creates the spam variable
# -The def statement defines the sayHello() function
# -The sayHello9'Al') line calls the now-created function, sending the execution to the top of the function's code
    # -This function call is also known as 'passing' the string value 'Al' to the function
# -A value passed to a function in a function call is an 'argument'
#   -The argument 'Al' is assigned to a local variable named 'name'
#   -Variables that have arguments assigned to them are 'parameters'

# ________________


# Return Values and Return Statements

# -When you call the len() function and pass it an argument like 'Hello', the function call evaluates to the integer value 5.
# -Generally, the value that a function call evaluates to is called the 'return value' of the function
# -When creating a function using the def statement, you can specify what the return value should be with a 'return statement'
# -Return statements consist of:
    # 1. The return keyword
    # 2. The value or expression that the function should return

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# 1. Python first imports the 'random' module
# 2. The getAnswer() function is defined
# 3. Because the function is defined, not called, the execution skips over the code in it
# 4. The random.randint() function is called with two arguments: 1 and 9
# 5. It evaluates to a random integer between 1 and 9. This value is stored in a variable named 'r'
# 6. The getAnswer function is called with r as the argument
# 7. The program execution moves to the top of the getAnswer() function
# 8. The value r is stored in a parameter named answerNumber
# 9. Depending ont he value in answerNumber, the function returns one of many possible string values
# 10. The program execution returns to the line at the bottom of the program that orginally called getAnswer
# 11. The returned string is assigned to a variable named 'fortune'
# 12. This variable gets pased to a print() call and is printed to the screen

# Can be further conslidated:

print(getAnswer(random.randint(1, 9)))