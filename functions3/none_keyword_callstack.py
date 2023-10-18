# The None Value

# -In Python there is a value called 'None' which represents the absence of a value
# -The None value is the only value of the NoneType data type
    # -Other languages call this null, nil, or undefined
# -Just like Boolean True and False values, None must be typed with a capital N
# -Helpful for when you need to store something that won't be confused for a real value in a variable
# -Used sometimes as the return value of print(), since print() function doesn't need to return anything in the same way len() or input() does

spam = print('Hello!')
None == spam

# -BTS Python adds return None to the end of any function definition with no return statement
    # -Similar to how 'while' or 'for' loops implicitly end with a 'continue' statement


#____________________________


# Keyword Arguments and the print() Function

# -Most argumnets are identified by their position in the function call.
    # -random.randint(1, 10) is different from random.randint(10, 1)
# -Rather than through their position, 'keyword arguments' are often used for 'optional parameters'
# -print() function has optional parameters 'end' and 'sep' to specify what should be printed at the end of its arguments and between its arguments

print('Hello')
print('World')

# >>> Hello
# >>> World

# -Printed to separate lines because print() automatically adds a newline character to the end of the string it is passed
# -However, 'end' keyword argument can change the new-line character to a different string

print('Hello', end='')
print('World')

# -The output is printed on a single line because there is no longer a newline printed after 'Hello'.
    # -The blank string is printed instead

# -When you pass multiple string values to print(), the function auto separates them with a single space

print('cats', 'dogs', 'mice')
# >>> cats dogs mice

# -Replace the default separating string by passing the 'sep' keyword argument a diff string

print('cats', 'dogs', 'mice', sep=',')

# -You can add keyword arguments to your own functions, but need to learn about list and dictionary data types first

#_____________________________


# The Call Stack

# -Calling a function doesn't send the execution on a one-way trip to the top of a function
    # -Python remembers which line of code called the function so the execution can return there when it hits a 'return' statement
    # -If the original function called other functions, the execution returns to those function calls first, before returning to OG function call

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# 1. When a() is called, it calls b(), which in turn calls c()
# 2. The c() function doesn't call anything, just displays c() starts and c() returns before returning to the line in b() that called it
# 3. Once execution returns to the code in b() that called c(), it returns to the line in a() that called b()
# 4. Execution continues to the next line in the a() function, which is a call to d()
    # -Like the c() function, the d() function doesn't call anything. Just displays d() starts and d() returns before returning to the line in a() that called it
# 5. Since d() contains no other code, the execution returns to the line in a() that called d()
# 6. The last line in a() displays a() returns before returning to the original a() call at the end of the program

# -The call stack is how Python remembers where to return the execution after each fucntion call.
    # -Python handles call stack not in a variable in the computer, but behind the scenes
# -When my program calls a function, Python creates a 'frame object' on the top of the call stack
# -Frame objects store the line number of the original function call
# -When a fucntion call returns, Python removes a frame object from the top of the stack and moves the executjio to the line number stored in it
    # -Note: Frame objects are always added and removed from the top of the stack, never from any other place
# -The top of the call stack is which function the execution is currently in
    # -When the call stack is empty, the execution is on a line outside of all functions
