
class Animal:
    def eat(self):
        print("Animals eat......")

class Bird(Animal):
    def fly(self):
        print("Birds fly....")

class Chicken(Bird):
    def disp(self):
        print("Chickens are breeded for consumption.....")

    def fly(self):
        print("Chickens very rarely fly.....")

chick = Chicken()
chick.disp()
chick.fly()
chick.eat()
