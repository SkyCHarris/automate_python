
#! References

# Variables store strings and integer values. But this is a simplified explanation
# Technically variables are storing references tot he computer memory locations where the values are stored

spam = 42
cheese = spam
spam = 100
spam
cheese

# When you assign 42 to the spam variable, you are creating the 42 value in the computer's memory and storing a reference to it in the spam variable
# When you copy the value in spam and assign it to variable cheese, you're copying the reference
# Both spam and cheese refer to the 42 value in the computer's memory
# When later change the value in spam to 100, you're creating a new 100 value and storing a reference to it in spam
    # This doesn't affect the value in cheese
# Integers are immutable values, they don't change
# Changing the spam variable is making it refer to a different value in memory

# Lists don't work this way, because list values can change. They are mutable

spam = [0, 1, 2, 3, 4, 5]
cheese = spam # The reference is being copied, not the list
cheese[1] = 'Hello!' # This changes the list value
spam
cheese # The cheese variable refers to the same list

# This may look odd. The code touched only the cheese list, but it seems that both the cheese and spam lists have changed
# When you create the list:
    # 1. You assign a reference to it in the spam variable
    # 2. But the next line copies only the list reference in spam to cheese, not the list value itself
        # 2.a. The values stored in spam and cheese now both refer to the same list
        # 2.b. There is only one underlying list because the list itself was never actually copied
    # 3. When you modify the first element of cheese, you are modifying the same list that spam refers to

# Variables are like boxes that contain values. The previous figures in this chapter show that lists in boxes aren't exactly accurate, becaus elist variables don't contain lists-
    # They contain references to lists
    # These references will have ID numbers that Python uses internally


#? Identity and the id() Function

# Why doesn't the weird behavior with mutable lists in the previous chapter happen with immutable values like integers or strings?
    # Python's id() function helps us understand this
# All values in Python have a unique identity that can be obtained with the id() function

id('Howdy')

# When Python runs id('Howdy') it creates the 'Howdy' string in the computer's memory
# The numeric memory address where the string is stored is returned by the id() function
# Python picks this address based on which memory bytes happen to be free on your computer at the time

# Like all strings, 'Howdy' is immutable and cannot be changed
    # If you 'change' the string in a variable, a new string object is being made at a different place in memory, and the variable refers to this new string
    # ex. Enter the code and see how the identity of the string referred to by bacon changes

bacon = 'Hello'
id(bacon)
bacon += ' world!' # A new string is made from 'Hello' and ' world!'.
id(bacon) # bacon now refers to a completely different string.

# But lists can be modified since they are mutable objects
# The append() method doesn't create a new list object- it changes the existing list object
    # This is called 'modifying the object in-place'

eggs = ['cat', 'dog'] # This creates a new list
id(eggs)
eggs.append('moose') # append() modifies the list 'in place'.
id(eggs) # eggs still refers to the same list as before
eggs = ['bat', 'rat', 'cow'] # This creates a new list, which has a new identity
id(eggs) # eggs now refers to a completely different list

# If two variables refer to the same list (like spam and cheese) and the list value itself changes, both variables are affected
# append(), extend(), remove(), sort(), reverse(), and other list methods modify lists in place


#? Passing References

# References are important for understanding how arguments get passed to functions
    # When a function is called, the values of the arguments are copied to the parameter variables
    # For lists (and dictionaries), this means a copy of the reference is used for the parameter

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# When eggs() is called, a return value is not used to assign a new value to spam
    # Instead, it modifies the list in place, directly.
# Even though spam and someParameter contain separate references, they both refer to the same list
    # This is why the append('Hello') method call inside the function affects the list even after the function call has returned


#? The copy Module's copy() and deepcopy() Functions

# Passing around references is often the handiest way to deal wtih lists and dictionaries
    # However, if the function modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary value
    # Python provides a module named 'copy' that provides both the copy() and deepcopy() functions
# Copy: copy.copy(): can be used to make a duplicate copy of a mutable value, like a list or dictionary, not just a copy of a reference

import copy
spam = ['A', 'B', 'C', 'D']
id(spam)
cheese = copy.copy(spam)
id(cheese) # cheese is a different list with different identity
cheese[1] = 42
spam
cheese

# The spam and cheese variables now refer to separate lists. That's why only the list in cheese is modified when you assign 42 at index 1
# The reference ID numbers are no longer the same for both variables. They refer to independent lists
# If the list you need to copy contains lists, use the copy.deepcopy() function isntead of copy.copy()
    # deepcopy() will copy these inner lists as well