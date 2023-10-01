# Write a function named collatz() that has one parameter named 'number'
# If number is even, collatz() should print number // 2 and return this value
# If number is odd, collatz() should print and return 3 * number + 1

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)           
        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)

# Then write a program that lets the user type in an integer and keeps calling collatz() on that number until the function returns the value 1.
# Remember to convert return value from input() to an integer

user_number = int(input("Type any integer"))
collatz(user_number)




