
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return f"The price is {self.__price}"

    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be less than zero.....")
        else:
            self.__price = val

import sys
try:
    pepsi = Product(50)
    print(pepsi.get_price())
    pepsi.set_price(75)
    print(pepsi.get_price())

except ValueError:
    print("Exception Occured......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])