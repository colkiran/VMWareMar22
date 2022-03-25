
class Employee:
    def __init__(self, name):
        print("Employee Ctor.....")
        self.name = name
        self.__desig = "MGR"             # private variable
        self._dept = "HR"                # protected variable
        self.e = 100


class Manager(Employee):
    def __init__(self, name):
        print("Manager Ctor......")
        super().__init__(self)
        self.name = name
        self._age  = 45

    def __str__(self):
        # return f"name is {self.name} \ndept is {self._dept} \ndesig is {self.__desig}"
        return f"name is {self.name} \ndept is {self._dept}"


emp1 = Manager("Mike")
print(emp1)
print(emp1.__dict__)
print("Age :emp1._age")

