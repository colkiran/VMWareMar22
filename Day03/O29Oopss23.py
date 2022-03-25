
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):
    def doJob(self):
        print("Developer's Job......")

def BankFun(emp):           # polymorphism
    print("Bank job started......")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 40)

Mike = Manager()
Dave = Developer()

BankFun(Mike)
BankFun(Dave)

def BankFunJobs(emps):           # polymorphism
    print("Bank job started......")

    for emp in emps:
        emp.doJob()

    print("Bank job ended......")
    print("-" * 40)

BankFunJobs([Mike, Dave])
