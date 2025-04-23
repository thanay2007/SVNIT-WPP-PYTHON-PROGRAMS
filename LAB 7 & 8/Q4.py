class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + ' & ' + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return self.salary - other.salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

e1 = Employee("Thanay", 500000)
e2 = Employee("Arnav", 300000)
combined = e1 + e2
salary_diff = e1 - e2
print(combined)
print("Salary difference:", salary_diff)
