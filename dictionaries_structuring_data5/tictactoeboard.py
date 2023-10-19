
#! A Tic-Tac-Toe Board

# A tic-tac-toe board looks like a large hash symbol (#) with nine slots that each can contain an X, an O, or a blank
# To represent the board with a dictionary you can assign each slot a string-value key

'top-L' 'top-M' 'top-R'

'mid-L' 'mid-M' 'mid-R'

'low-L' 'low-M' 'low-R'

# Use string values to represent what' sin each slot on the board:
    # 'X', 'O', or ' ' (a space)
# You'll need to store nine strings
    # You can use a dictionary of values for this
# The string value with the key 'top-R' can represent the top-right corner, the string value with the key 'low'L' can represent the bottom-left corner, 'mid-M' can represent the middle, etc.

# This dictionary is a data structure that represents a tic-tac-toe board
# Store this board-as-a-dictionary in a variable named theBoard.

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# This data structure in theBoard variable represents a blank tic-tac-toe board

# Since the value for every key in theBoard is a single-space string, this dictionary represents a completley clear board
# If player X went first and chose the middle space, you could represent that board with:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Now we have a tic-tac-toe board with an X in the 'mid-M' key value spot

# Here's an example of when player O has won by placing O's across the top of the board:

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

# The player sees only what is printed to the screen, not the contents of variables
# Let's create a function to print the board dictionary onto the screen:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

# The printBoard() function can handle any tic-tac-toe data structure you pass it
# Try the following code:

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

# Because we created a data structure to represent a tic-tac-toe board and wrote code in printBoard() to interpret that data structure...
    # ...we now have a program that 'models' the tic-tac-toe board
# We could have organized our data structure differently (using keys like 'TOP-LEFT' instead of 'top-L') but as long as the code works with our data structures we'll have a correctly working program

# The printBoard() function expects the tic-tac-toe data structure to be a dictionary with keys for all nine slots
    # If the dictionary we passed was missing the 'mid-L' key, our program would no longer work

# Now let's add code that allows players to enter their moves:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# The new code:
    # 1. Prints out the board at the start of each new turn
    # 2. Gets the active player's move
    # 3. Updates the game board accordingly
    # 4. Swaps the active player
    # 5. Moves on to the next turn

# This isn't a complete tic-tac-toe game. It doesn't ever check whether a player has won
    # But it's enough to see how data structures can be used in programs