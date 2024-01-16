
#! Variable Scope - Understanding the LEGB Rule and Global/Nonlocal Statements

'''
LEGB
Local, Enclosing, Global, Built-in
'''

# Local -> variable defined within a function
# Enclosing -> variables in a local scope of enclosing functions
# Global -> variables defined at top-level of module, explicitly declared
# Built-in -> pre-assigned python variables

# Python checks these in order

x = 'global x'  # global

def test():
    y = 'local y'   # local
    # print(y)
    print(x)

test()

# Even though we're within our test function, we printed global x
# Checks local -> checks enclosing -> checks global -> bingo
    # Doesn't go both ways

x = 'global x'  # global

def test():
    y = 'local y'   # local
    # print(y)
    print(x)

test()
print(y)

# y variable doesn't live outside of test function

x = 'global x'

def test():
    y = 'local y'
    # print(y)
    print(x)

test()
print(x)

# Change 'local y' to 'local x'

x = 'global x'

def test():
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)
# global x is not overwritten. local x variable lives only within the function

# Set new value for global x

x = 'global x'

def test():
    global x    # working with global x variable
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)

# Arguments/Parameters

def test(z):    # z exists only within function
    x = 'local x'
    # print(y)
    print(z)

test('local z')
print(z)    # throws error, wrong scope

# Built-in

m = min([5,1,4,2,3])
print(m)

# View variables within the built-in scope

import builtins

print(dir(builtins))
# be careful not to override builtins

# Enclosing
# Nested functions

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
# checks first for local variables, then for variables in enclosing scope (outer function)

# Enclosing Scope Variables
# Change x variable of our outer function
    # Shouldn't use global, will affect our global scope
# nonlocal

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
# nonlocal more useful than global?

x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)