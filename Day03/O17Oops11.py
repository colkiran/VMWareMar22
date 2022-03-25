
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

emp1 = Employee("Mike", 50000)
print(emp1)

print(len(emp1))

print("-" * 40)
print([t for t in emp1])
