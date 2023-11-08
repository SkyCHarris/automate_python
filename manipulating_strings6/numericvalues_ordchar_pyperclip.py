
#! Numeric Values of Characters with the ord() and chr() Functions

# Computers store information as bytes- strings of binary numbers, which means we need to be able to convert text to numbers
# Because of this, every text character has a corresponding numeric value called a 'Unicode code point'
    # ex. The numeric code point is 65 for 'A', 52 for '4', and 33 for '!'
# you can use the ord() function to get the code point of a one-character string, and the chr() function to get the one-character string of an integer code point

ord('A')
ord('4')
ord('!')
chr(65)

# These functions are useful when you need to do an ordering or mathematical operation on characters:

ord('B')
ord('A') < ord('B')
chr(ord('A'))
chr(ord('A') + 1)
