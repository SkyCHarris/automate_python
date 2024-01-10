
#! Conditionals and Booleans

# Comparisons:
# Object Identity: is
    # Do objects have the same id, or are they the same in memory

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

# 2nd evaluates to false bc 2 diff objects in memory
# Print out locations with built-in id function

a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b)

#* False Values

# False
# None
# Zero of any numeric type
# Any empty sequence. '', (), []
# Any empty mapping. {}