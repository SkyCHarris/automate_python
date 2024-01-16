
#! Sorting Lists, Tuples, and Objects

# How to sort in Python, diff. datatypes

# sorted()

li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

# Sort original list of numbers without creating a new variable

# sort()

li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('Sorted Variable:\t', s_li)

li.sort()

print('Original Variable:\t', li)
# sorts the original list of integers

# sorted() -> returns new sorted list, can be set to variable
# sort() -> sorts list in place, returns None

# Sort in Descending Order

li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li, reverse=True) # descending order

print('Sorted Variable:\t', s_li)

li.sort(reverse=True)   # can also descend here

print('Original Variable:\t', li)

# Why choose sorted() over sort()
# More flexibility. Pass in any iterable
    # sort() only works on lists

tup = (9,1,8,2,7,3,6,4,5)
# no sort() method
s_tup = sorted(tup)
print("Tuple\t", s_tup)
# returns list of values in tuple, sorted

# Dictionaries

di = {'name': 'Sky', 'job': 'engineer', 'age': None, 'os': 'Windows'}
s_di = sorted(di)
print('Dict\t', s_di)
# sorts keys

# Sort on Criteria Other than Ascending/Descending

# Absolute Value
# key parameter

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print (s_li)
# runs each element through absolute value function before making comparison

# Sort Named Attributes

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # tells python how we want function represented when printed to screen
        return '({},{},${}'.format(self.name, self.age, self.salary)
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)
print(s_employees)
# sort based on name