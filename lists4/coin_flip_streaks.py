
#! Coin Flip Streaks

# For this exercise, try doing an experiment.
# If you flip a coin 100 times and write down an "H" for each heads and "T" for each tails, you'll create a list that looks like:
    # "TTTTHHHHTT"
# If you ask a human to make up 100 random coin flips, you'll end up with alternating head-tail results like:
    # "HTHTHHTHTT"
        # This looks random to humans, but isn't mathematically random
        #TODO 1. import random, random.randomint() method for coin flip
    # A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails
# Your program breaks up the experiment into 2 parts:
    # 1. Generate a list of randomly selected 'heads' and 'tails' values
    #TODO 2. function that randint(1,2) 100 times. use i = i + i counter to count totals?
    # 2. Check if there is a streak of 6 in it
    #TODO 3. Unsure how to check for streak currently
    # 3. Put all of this code in a loop that repeats the experiment 10,000 times to find out what percentage of the coin flips contain a streak of six heads or tails in a row
    #TODO 4. Repeat the 100x experiement 10000 times...
    # HINT: The function call random. randint(0,1) will return a 0 value 50% of the time and a 1 value the other 50% of the time

#? Code Sample
import random
numberOfStreak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values


    # Code that checks if there is a streak of 6 heads or tails in a row
    
import random
numberOfStreaks = 0
h_streak = 0
t_streak = 0

headsOrTails = []
for i in range(100):
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        headsOrTails.append("H")
    elif coin_flip == 1:
        headsOrTails.append("T")
    for i in headsOrTails:
        if i == "H":
            h_streak = h_streak + 1
        elif i == "T":
            t_streak = t_streak + 1
    print(h_streak, t_streak)

# Attempt 2

import random
total_h_streak = 0
current_h_streak = 0
total_t_streak = 0
current_t_streak = 0

for i in range(100):
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        current_h_streak = current_h_streak + 1
        if current_h_streak >= 6:
            total_h_streak = total_h_streak + 1
    elif coin_flip == 1:
        current_t_streak = current_t_streak + 1
        if current_t_streak >=6:
            total_t_streak = total_t_streak + 1
    print(total_h_streak, total_t_streak)

#TODO Unfinished

        
