
#! Comma Code

# You have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space
    # Insert 'and' before the last item
    #ex. 'apples, bananas, tofu, and cats'
# Remember to test an empty list [] case

def comma_code(lst):
    sliced_list = str(lst[0, -1])
    return sliced_list

comma_code(['apples', 'bananas', 'tofu', 'cats'])


# Attempt 2

def comma_code(lst):
    for i in lst:
        print(str(i[0:-1]) + 'and')
    
comma_code(['apples', 'bananas', 'tofu', 'cats'])


# Attempt 3

def comma_code(lst):
    for i in lst:
        list_items = str(lst[0:-1])
        print(list_items)

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)

# Attempt 4

def comma_code(lst):
    for i in lst:
        list_ordered = str(lst[0,-1]) + 'and' + str(lst[-1])
        print(list_ordered)

comma_code(['apples', 'bananas', 'tofu', 'cats'])

# Attempt 5
# https://www.youtube.com/watch?v=GRVMCziIjS4

def commaCode(lst):
    empty = ''
    if len(lst) == 0:
        return "Invalid list. Try again"
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return (lst[0] + ' and ' + lst[-1])
    elif len(lst) > 2:
        for i in range(len(lst) -1):
           empty += (lst[i] + ', ')
        empty += ('and ' + lst[-1])

        return empty

spam = ['apples', 'bananas', 'tofu', 'cats']
empty = commaCode(spam)
print(empty)