# A Short Program: Guess the Number

# -Program output will look something like this

# >> I am thinking of a number between 1 and 20.
# >> Take a guess.
10
# >> Your guess is too low.
# >> Take a guess.
15
# >> Your guess is too low.
# >> Take a guess
17
# >> Your guess is too high.
# >> Take a guess
16
# >> Good job! You guesse dmy number in 4 guesses!

# ____________________________


# This is a guess the number game

import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number betwen 1 and 20.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
     print('Your guess is too low.')
    elif guess > secretNumber:
     print('Your guess is too high')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# 1. Program imports the 'random' module so that it can use the random.randit() function
# 2. The return value, a random integer between 1 and 20, is stored in the variable 'secretNumber'
# 3. Program tells player to come up with a secret number. Gives 6 chances to guess
# 4. The code that lets the player enter a guess, and checks that guess, is in a for loop. Will loop at most 6 times
# 5. First thing to happen in the loop is that the player types in a guess
# 6. input() returns a string, which we pass to int() to translate string to integer
# 7. This guess gets stored in a variable named 'guess'
# 8. The if/elif statement inside the for loop checks to see whether the guess is less than or greater than the secret number. Hint provided
# 9. If the guess is neither higher nor lower, it must be equal to the secret number-- if so, break will take the program execution out of the for loop
# 10. After the for loops, the if...else statement checks whether the player has correctly guessed the number and then prints appropriate message
# 11. In both cases, the program displays a variable that contains an integer value (guessesTaken or screenNumber)
#       -Since we must concatenate these integers with a string, it passes the variables to a str() function
# 12. These strings are then passed to the print() function call