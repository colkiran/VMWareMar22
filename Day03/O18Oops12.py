
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'reactJS']

    def __str__(self):
        return "Name is {} and salary is {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        # return self.tech.__iter__()
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value


emp1 = Employee("Louis", 36)
print(emp1)

print("-" * 40)

print([tech for tech in emp1])

print("-" * 40)
emp1.append("python")

print([tech for tech in emp1])
print("-" * 40)

x = emp1[2]
print(f"x :{x}")

print("-" * 40)

# 'str' object does not support item assignment
# 'Employee' object does not support item assignment

emp1[1] = 'JSP'
print([tech for tech in emp1])