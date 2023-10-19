
#! Pretty Printing

# Importing the pprint module into your program gives you access to the pprint() and pformat() functions
    # They will "pretty print" a dictionary's values
# This is helpful when you want a cleaner display of the items in a dictionary than what print() provides

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries
# To obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat()
# These two lines are equivalent:

pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))

#! Using Data Structures to Model Real-World Things

# Even before the internet it was possible to play a game of chess with someone on the other side of the world
# Each person would set up a chessboard at their home then mail postcards to each other describing each move
    # To do this, players needed a way to unambiguously describe the state of the board and their moves

# In algebraic chess notation the spaces on the chessboard are identified by a number and letter coordinate

# The chess pieces are identified by letters: K: king, Q: queen, R: rook, B: bishop, N: knight.
# Describing a move uses the letter of the piece and the coordinates of its destination
    # A pair of these moves describes what happens in a single turn (white goes first)
        # ex. The notation 2. Nf3 Nc6 indicates that white moved a knight to f3 and black moved a knight to c6 on the second turn of the game
# With algebraic notation you can unambigously describe a game of chess without needing to be in front of a chessboard

# A program on a modern computer can easily store billions of strings like Nf3 Nc6
    # This is how computers play chess without having a physical chessboard
    # They model data to represent a chessboard, and we can write code to work with this model
# This is where lists and dictionaries come in

{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# Represent the chess board in figure 5-2 (p. 120)

# We'll use tic-tac-toe instead, which is simpler