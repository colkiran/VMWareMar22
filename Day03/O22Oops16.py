
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("getter called....")
        return f"The price is {self.__price}"

    def set_price(self, val):
        print("setter called.....")
        self.__price = val

    def del_price(self):
        print("deleter called.....")
        self.__price = 0

    price = property(get_price, set_price, del_price)

coke = Product(65)
print(coke.price)
coke.price = 57
prc = coke.price
print(prc)

del coke.price
print(coke.price)

