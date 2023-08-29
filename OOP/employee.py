# Create empty class and skip for now
class Employee: 
    # Class Variables
    raise_amt = 1.04

    # Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # Method to print fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Subclass of Employee: Developer
class Developer(Employee):
    raise_amt = 1.10 # change raise amount in subclass not changing anything in parent class Employee
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # pass in first, last, and pay from Employee __init__ method
        # Employee.__init__(self, first, last, pay) <- another way of using parent's constructor
        self.prog_lang = prog_lang


class Manager(Employee):
    # Constructor
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) # pass in first, last, and pay from Employee __init__ method
        if employees is None:
            self.employees = [] # create an empty list if employees are not provided
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# Create 2 objects of Employee
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False

print(isinstance(Manager, Employee)) # True
print(isinstance(Manager, Developer)) # False

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
