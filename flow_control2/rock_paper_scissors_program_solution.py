# Short Program: Rock, Paper, Scissors

import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0


while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:

    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove =='r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print ('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
        
# 1. import 'random' and 'sys' modules so that the program can call random.randint() and sys.exit() functions
# 2. Set up 3 variables to track wins, losses, and ties for the player
# 3. This program uses a while loop inside of another while loop
#       3a. First loop is the main game loop. A single game of rock, paper, scissors is played on each iteration through this loop.
#       3b. The second loop asks for input from the player, and keeps looping until the player has entered r, p, s, or q
# 4. r, p, s, correspond to rock, paper, scissors. q corresponds sys.exit() function call
# 5. If the player enters r, p, or s, the execution breaks out of the loop. Otherwise the program reminds the player to enter correctly
# 6. The player's move is printed to the screen
# 7. Next, the computer's move is randommly selected vis random.randint()
# 8. 1, 2, or 3 integer it returns is stored in the variable randomNumber
# 9. computerMove stores 'r', 'p', or 'q' string based on integer in randomNumber, then displays the computer's move
# 10. The program compares the strings in playerMove and computerMove, then prints the results
# 11. The program increments wins, losses, or ties based on game round result
# 12. Once execution reaches the end, it jumps back to the start of the main program loop to begin another game