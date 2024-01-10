
#! Loops and Iterations

nums = [1, 2, 3, 4, 5]

# Break: completely breaks out of a loop
# Continue: moves onto next iteration of the loop

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# We're looking for a certain # in our list. Once found, don't need to continue looping

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# What if we want to ignore a value, but not break out of a loop completely?
    
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Loop w/in loop
# Loops through every letter in the string, then moved to next # and did same thing
    
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

# Range
# Run through a loop a certain amount of times

for i in range(10):
    print(i)

# While loops
# Keep going until certain condition is met, or a break
    
x = 0
while x < 10:
    print(x)
    x += 1

# At any point, use break to break out of while loop
    
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# May want an infinite loop until we get some input or value
    
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1