
# duck types

class Manager:
    def doJob(self):
        print("Manager Job....")

class Developer:
    def doJob(self):
        print("Developer Job.....")

manoj = Manager()
devi = Developer()

def BankFunJobs(emps):           # polymorphism
    print("Bank job started......")

    for emp in emps:
        emp.doJob()

    print("Bank job ended......")
    print("-" * 40)

BankFunJobs([manoj, devi])
