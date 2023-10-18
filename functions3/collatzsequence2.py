

def collatz(number):
    while number != 0:
        if number % 2 == 0:
            new_number = number //2
            print(new_number)
        elif number % 2 == 1:
            new_number = 3 * number + 1
            print(new_number)
    
user_number = int(input("Type an integer"))

collatz(user_number)