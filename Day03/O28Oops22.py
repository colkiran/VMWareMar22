
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account...")

    def deposit(self, amt):
        print(f"{amt} deposited......")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def transfer(self, amt):
        print(f"{amt} transferred......")

    def getBalance(self):
        print(f"The balance in the account is #####.##")

perAcnt = Savings()
perAcnt.getBalance()