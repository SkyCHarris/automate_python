# A Short Program: Zigzag

# Let's create a small animation program. It will create a back-and-forth zigzag pattern until the user stops it by pressing the Stop button or CTRL-C

import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

# 1. First, import the time and sys modules with two variables:
    # 1a. indent variable keeps track of how many spaces of indentation are before the asterisks
    # 1b. indentIncreasing contains a Boolean to determine if the amount of indentation is increasing or decreasing
# 2. Next, place the rest of the program inside a try statement
    # 2a. When users presses CTRL-C, Python raises the KeyboardInterrupt exception
    # 2b. With no try-except statement, the program crashes. Ugly error message. So call sys.exit()
# 3. The while True: infinite loop repeats instructions in the program forever. Uses '' * indent to print the correct amount of spaces of indentation
    # 3a. We don't want to automatically print a newline after these spaces, so we pass end='' to the first print() call
    # 3b. A second print() call prints the band of asterisks
# 4. The time.sleep() function introduces a one-tenth-second pause in the program
# 5. Next, adjust the amount of indentation for the next time we print asterisks
    # 5a. If indentIncreasing is True, we want to add one to indent.
    # 5b. Once it reaches 20, we want the indentation to decrease
# 6. If indentIncreasing is false, we want to subtract one from indent
    # 6a. Once indent reaches 0, we want the indentation to increase once again
    # 6b. Either way, the program execution jumps back to the start of the main program loop to print asterisks again
# 7. If the user presses CTRL-C at any point program execution is in the try block, KeyboardInterrup exception is raised and handled by the except statement
# 8. Program execution moves indie the except block, which runs sys.exit() and quits the program