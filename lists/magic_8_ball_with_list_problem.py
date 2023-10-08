
#! Example Program: Magic 8 Ball with a List

# Using lists, you can write a mmuch more elegant version of the previous chapter's Magic 8 Ball program
# Instead of several lines of nearly identical elif statements, create a single list that the code works with

import random

messages = ['It is certain',
            'It is decidedly so'
            'Reply hazy, try again'
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) -1)])

# When you run this program, you can see that it works the same as the previous
# The expression used as the index for messages: random.randint(0, len(messages) - 1)
    # Produces a random number to use for index, regardless of the size of messages
    # You'll get a random number between 0 and the value of len(messages) - 1
# The benefit to this is that you can add or remove strings to the messages list without changing the other lines of code