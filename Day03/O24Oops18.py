
"""
class
object
isinstance
__init__, __del__
self
class attribute
@classmethod
cls
__str__
__eq__, __gt__, __add__, __sub__......
private variables with __
__dict__
property, @property -> setter getter and deleter
"""

class Animal:
    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

# inheritance
class Bird(Animal):
    def fly(self):
        print("Birds fly")

class Fish(Animal):
    def swim(self):
        print("Fishses swim")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print(cuckoo.__dict__)

print("-" * 40)
dolphin = Fish()
dolphin.swim()
dolphin.eat()
print(dolphin.__dict__)








