# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Subclass Manager
class Manager(Employee):
    def calculate_salary(self):
        bonus = 5000
        return self.base_salary + bonus


# Subclass Developer
class Developer(Employee):
    def calculate_salary(self):
        bonus = 3000
        return self.base_salary + bonus


# Subclass Intern
class Intern(Employee):
    def calculate_salary(self):
        deduction = 1000
        return self.base_salary - deduction


# Creating objects
m = Manager("Rahul", 50000)
d = Developer("Anu", 40000)
i = Intern("Arjun", 20000)

employees = [m, d, i]

# Display salary details
for emp in employees:
    print("Name:", emp.name)
    print("Final Salary:", emp.calculate_salary())
    print()