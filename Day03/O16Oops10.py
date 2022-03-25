
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name :{self.name}\nSalary :{self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


em1 = Employee("Jack", 100000)
em2 = Employee("Jane", 90000)

print(f"Add Salary: {em1 + em2}")
print(f"Sub Salary: {em1 - em2}")
print(f"Mul Salary: {em1 * em2}")
print(f"Div Salary: {em1 / em2}")
print(f"Floor Div Salary: {em1 // em2}")

"""
1. add +
2. sub -
3. mul *
4. div /
5. floordiv //
"""