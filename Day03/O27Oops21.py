
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")

    def eat(self):
        print("Animals eat....")

    def fun(self):
        print("Fun method of Animal class...")

class Person:

    def __init__(self):
        self.p = 20
        print("Person Ctor....")

    def Talk(self):
        print("Person Talks......")

    def fun(self):
        print("Fun method of Person class...")

class Girl(Animal, Person):

    def __init__(self):
        self.g = 30
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor.....")



jane = Girl()
jane.fun()
print(jane.__dict__)
