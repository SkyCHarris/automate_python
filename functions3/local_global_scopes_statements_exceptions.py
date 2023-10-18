# Local and Global Scope

# -Parameters and variables assigned in a called function are said to exist in that function's 'local scope'
# -Variables that are assigned outside all functions are said to exist in the 'global scope'
# -These are local variables and global variables
    # -A variable must be one or the other, cannot be both

# -Think of a scope as a container for variables. When a scope is destroyed, all values stored in the scope's variables are forgotten
# -There is only one global scope
# -A local scope is created when a function is called
# -When the function returns, the local scope is destroyed, and the variables are forgotten
# -Local variables are also stored in frame objects on the call stack

# -Python has different scopes so that when variables are modified by the code in a call to a function, the function interacts with the rest of the program only through its parameters and the return value.
# -This narrows down the number of lines of code that may be causing a bug


# Local Variables Cannot Be used in the Global Scope

def spam():
    eggs = 31337
spam()
print(eggs)

# -Program outputs an error. Once the program execution returns from spam, that local scope is destroyed, and there is no longer a variable named eggs


# Local Scopes Cannot Use Variables in Other Local Scopes

# -A new local scope is created whenever a function is called, including when a function is called from another function

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# 1. Spam function is called, local scope is created
# 2. Local variable eggs is set to 99
# 3. Bacon function is called, second local scope is created
    # 3b. Multiple local scopes can exist at the same time
# 4. In new local scope, local variable ham is set to 101, and local variable eggs (different from the one in spam()'s local scope) is also created and set to 0
# 5. When bacon() returns, the local scope for that call is destroyed, including its eggs variable
# 6. Program execution continues in the spam() function to print eggs
# 7. Since the local scope for the call to spam() still exists, the only eggs variable is the spam() funciton's eggs variable, set to 99
# 8. The program prints this

# Global Variables Can Be Read from a Local Scope

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

# -There is no parameter named eggs or any code assigning eggs a value in the spam() function.
# -When eggs is used in spam(), Python references the global variable eggs and prints 42


# Local and Global Variables with the Same Name

# -It's technically fine to use the same variable name for a global variable and a local variable in different scopes in Python
# -Avoid this though

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

# -There are three different variables, but they're all confusingly named 'eggs'
# 1. A variable named eggs in a local scope when spam() is called
# 2. A variable named eggs in a local scope when bacon() is called
# 3. A variable named eggs in the global scope


# ___________________


# The global Statement

# -If you need to modify a global variable from within a function, use the 'global' statement
# -If you have a line such as 'global eggs' at the top of a function, it tells Python:
    # -"In this function, eggs refers to the global variable, so don't create a local variable with this name"

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

# -Because 'eggs' is declared global at the top of spam(), when eggs is set to 'spam', this assignment is done to the globally scoped eggs
# -No local variable eggs is created

# 4 rules to tell if a variable is in a local scope or global scope:
# 1. If variable is used in the global scope (outside all functions), it's always a global variable
# 2. If there is a global statement for that variable in a function, it is a global variable
# 3. Otherwide, if the variable is used in an assignement statement in the function, it is a local variable
# 4. If the variable is not used in an assignment statement, it is a global variable

def spam():
    global eggs
    eggs = 'spam' #global

def bacon():
    eggs = 'bacon' #local

def ham():
    print(eggs) #global

eggs = 42 #global
spam()
print(eggs)

# -In the spam() function, eggs is the global eggs variable because there's a global statement for eggs at the beginning of the function
# 1. In bacon(), eggs is local variable because there's an assignment statement for it
# 2. In ham(), eggs is the global variable because there is no assignment statement or global statement for it
# -In a function, a variable will either azlways be global or always be local.
# -The code in a function can't use a local variable named eggs and then use the global eggs variable later in that same function

def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()

# 1. Python sees that there is an assignment statement for eggs in the spam() function
# 2. Considers eggs to be local
# 3. But print(eggs) is executed before eggs is assigned anything, and the local variable eggs doesn't exist
# 4. Python will NOT fall back to using the global eggs variable


# ___________________

# Exception Handling

# -Getting an error, or exception, in your Python program means the entire program will crash
# -Don't want this to happen in real-world programs
# -Instead, get the program to detect errors, handle them, and then continue to run

# -The following program has a divide-by-zero error

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# -We defined a function called spam, given it a parameter, and printed the value of that function with various parameters to see what happens
# -ZeroDivisionError happens when you try to divide a number by 0
# -Errors can be handled with try and except statements. Code that could potentially have an error is put in a try clause
# -Program execution moves to the start of a following except clause if an error happens

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# -When code in a try clause causes an error, the program execution immediately m oves to the code in the except clause.
# -After running that code, the execution continues as normal
# -Following code insteead has the spam() calls in the try block

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

# -print(spam(1)) is never executed because once the execution jumps to the code in the except clause, it does not return to the try clause.
# -It instead continues moving down the program as normal