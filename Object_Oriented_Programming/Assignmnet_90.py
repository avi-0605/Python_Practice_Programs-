# Class Employee **with Inheritance Base class Employee (name, ID, salary) and child class Manager (with additional attributes). Override a method in the subclass.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    # Overriding the display_details method
    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}, Department: {self.department}")

# Creating instances
emp = Employee("John Doe", 101, 50000)
manager = Manager("Alice Smith", 102, 70000, "HR")

# Calling methods
print("Employee Details:")
emp.display_details()

print("\nManager Details:")
manager.display_details()