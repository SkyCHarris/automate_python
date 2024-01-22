
#! Python OOP Tutorial 1: Classes and Instances

# Create and use classes within Python
# How object-oriented concepts are implemented

# Basics of creating and instantiating simple classes

# Why use classes?
    # Allow us to logically group our data and functions in a way that's easy to reuse and build upon
    # Data and functions here called 'attributes' and 'methods'

# We have an app for our company. Want to represent employees in our Python code
    # Great for class. Each employee has specific attributes and methods
    # Name, email, pay, actions they can perform
# Have a class as a blueprint for employees

#* Create class

class Employee:
    pass
# simple Employee class with no attributes or methods

# Diff between class and instance of a class
# Class: blueprint for creating instances
# Instance: each unique employee created with this class is an 'instance' of this class

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
# both are employee objects with unique locations in memory

#* Instance variables
# Contain data that is unique to each instance
# Can manuall create instance variables for each employee

# Give employee 1 firstname/lastname

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50_000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60_000

print(emp_1.email)
print(emp_2.email)

# each of these instances have attributes that are unique to them

#* Set all of this info for each employee when they're created, rather than manually
# Lots of code, prone to mistakes done manually

#* init (initialize)
# When we create methods within a class, they receive the instance as the first argument automatically
# 'self' is the convention (can be w/e)

# When we set self.first = first, it's the same as saying emp_1.first = 'Corey
    # except now it's done automatically when we create employee objects

class Employee:
    def __init__(self, first, last, pay): # init method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee('Corey', 'Schafer', 50_000)  # When we create instances of employee class here, pass in values we specified in init method
emp_2 = Employee('Test', 'User', 60_000)  # Can leave off self, just need names and pay

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# Everything so far (name, email, pay) are all attributes of our class

#* Perform some kind of action
# Add methods to our class

# Display full name of employee:

class Employee:
    def __init__(self, first, last, pay): # init method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee('Corey', 'Schafer', 50_000)  # When we create instances of employee class here, pass in values we specified in init method
emp_2 = Employee('Test', 'User', 60_000)  # Can leave off self, just need names and pay

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(f'{emp_1.first} {emp_1.last}')    # Can be done here, BUT

#* Create method within our class that puts this functionality in one place
# method (aka function) def fullname

class Employee:
    def __init__(self, first, last, pay): # init method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'    # changed to self.first, self.last to work with all isntances


emp_1 = Employee('Corey', 'Schafer', 50_000)  # When we create instances of employee class here, pass in values we specified in init method
emp_2 = Employee('Test', 'User', 60_000)  # Can leave off self, just need names and pay

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) # need () because this is a method

#* Run methods using the class name itself

class Employee:
    def __init__(self, first, last, pay): # init method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}' 


emp_1 = Employee('Corey', 'Schafer', 50_000)  
emp_2 = Employee('Test', 'User', 60_000) 

emp_1.fullname()    # does same thing as below, but don't need to pass in self
print(Employee.fullname(emp_1)) # manually pass in instance as argument