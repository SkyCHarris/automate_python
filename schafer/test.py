
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