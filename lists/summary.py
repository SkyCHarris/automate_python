
#! Lists Chapter Summary

# Lists are useful data types that allow you to write code that works on a modifiable number of values in a single variable
    # Later we'll see programs using lists to do things that would be difficult or impossible to do without them
# Lists are a sequence data type that is mutable. Their contents can change
    # Tuples and strings, also sequence data types, are immutable and cannot be changed
    # A variable that contains a tuple or string value can be overwritten with a new tuple or string value, but it's not the same as modifying the existing value in place like with the append() or remove() methods for lists
# Variables do not store list values directly: they store references to lists
    # Important distinction when copying variables or passing lists as arguments in function calls
    # The value that is being copied is the list reference, so be aware that changes you m ake to the list might impact another variable in your program
# Use copy() or deepcopy() if you want to make changes to a list in one variable without modifying the original list