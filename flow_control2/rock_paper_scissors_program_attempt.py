# A Short Program: Rock, Paper, Scissors

# Output:

# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)rock (p)aper (s)cissors or (q)uit]
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)rock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)rock (p)aper (s)cissors or (q)uit
# q

import random, sys
wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')
player_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
bot_move = random.randint(1, 3)
# score = ('Wins ' + wins + 'Losses ' + losses + 'Ties ' ties) # <<<< Take a look here to continue!!!
score = wins, losses, ties


if player_move == 'r' and bot_move == 1:
    print("It's a tie!")
    ties = ties + 1
    print(score)
elif player_move == 'p' and bot_move == 1:
    print("You won this round! Gj.")
    wins = wins +1
    print(score)
elif player_move == 's' and bot_move == 1:
    print("Sorry, you lost this one.")
    losses = losses + 1
    print(score)
elif player_move == 'r' and bot_move == 2:
    print("Sorry, you lost this one.")
    losses = losses +1
    print(losses)
elif player_move == 'p' and bot_move == 2:
    print("It's a tie!")
    ties = ties + 1
    print(score)
elif player_move == 's' and bot_move == 2:
    print("You won this round! Gj.")
    wins = wins +1
    print(score)
elif player_move == 'r' and bot_move == 3:
    print("You won this round! GJ.")
    wins = wins + 1
    print(score)
elif player_move == 'p' and bot_move == 3:
    print("Sorry, you lost this one.")
    losses = losses + 1
    print(score)
elif player_move == 's' and bot_move == 3:
    print("It's a tie!")
    ties = ties + 1
    print(score)

elif player_move == 'q':
    sys.exit()
    








