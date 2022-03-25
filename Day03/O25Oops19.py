
class Animal:
    def __init__(self):
        print("Animal Ctor....")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat......")

# inheritance
class Bird(Animal):
    def __init__(self):             # overriding the parent class constructor
        print("Bird Ctor.....")
        super().__init__()
        self.size = '1k'

    def fly(self):
        print("Birds fly")

cuckoo = Bird()
print(cuckoo.__dict__)
print(cuckoo.age)
print(cuckoo.size)
