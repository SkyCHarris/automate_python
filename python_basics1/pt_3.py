# Your First Program

# This program says hello and asks for my name

print('Hello world!')
print('What is your name?)')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Dissecting Your Program

# -Programmers occasionally will 'comment out' code when testing a program

# The print() Function

# -The print() function displays the string value inside its parentheses on the screen

print('Hello world!')
print('What is your name?)')    # ask for their name

# -When Python executes this line, we say it is 'calling' the print() function and the string value is being 'passed' to the function
# -A value that is passed to a function call is an 'argument'

# The input() Function

# -The input() function waits for the user to type text and press 'ENTER'

myName = input()

# -This function call evaluates to a string equal to the user's text, and the line of code assigns the myName variable to this string value

# Printing the User's Name

print('It is good to meet you, ' + myName)

# -Expressions can always evaluate to a single value

# The len() Function

# -Pass the len() function a string value (or variable containing a string), and the function evalutes to the integer value of the number of char. in that string

print('The length of your name is:')
print(len(myName))

len('hello')
# >>> 5
len('My very energetic monster just scarfed nachos.')
# >>> 46
len('')
# >>> 0

# The str(), int(), and float() Functions

str(29)
# >>> '29'
print('I am ' + str(29) + ' years old.')
# >>> I am 29 years old.

str(0)
# >>> '0'
str(-3.14)
# >>> '-3.14'
int('42')
# >>> 42
int('-99')
# >>> -99
int(1.25)
# >>> 1
int(1.99)
# >>> 1
float('3.14')
# >>> 3.14
float(10)
# >>> 10.0

# -str() function is handy when you have an integer or float that you want to concatenate to a string.
# -int() function is helpful if you have a number as a string value that you want to use in some mathematics
#       ex. input() function always returns a string, even if the user enters a number

spam = input()
# >>> 101
spam
# >>> '101'

# -If you want to do math using the value in 'spam', use int() function to get the integer form of 'spam' and then store this as the new value in spam

spam = int(spam)
spam
# >>> 101

# -Now you can treat the 'spam' variable as an integer instead of a string

spam * 10 / 5
# >>> 202.0

print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Text and Number Equivalence

# -Integers and floating-points can be equal

42 == '42'
# >>> False
42 == 42.0
# >>> True
42.0 == 0042.000
# >>> True

# -In the next chapter we'll learn how to tell Python to make intelligent decisions about what code to run, what code to skip, and what code to repeat based on the values it has
# -This is known as 'flow control' and it allows us to write programs that make intelligent decisions