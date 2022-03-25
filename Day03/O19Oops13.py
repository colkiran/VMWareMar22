
class Employee:
    def __init__(self, name):
        self.__name = name                  # private variable
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'reactJS']

    def __str__(self):
        return "Name is " + self.__name + " and tech :" + ", ".join([tech for tech in self.tech])


emp1 = Employee('Kevin')
print(emp1)

# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Sameul"

print("-" * 40)
print(emp1)

