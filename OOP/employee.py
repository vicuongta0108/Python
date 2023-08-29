# Create empty class and skip for now
class Employee: 
    # Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # Method to print fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Create 2 objects of Employee
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

