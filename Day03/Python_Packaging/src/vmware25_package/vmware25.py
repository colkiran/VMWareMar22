
gname = "Sachin Tendulkar"

runs = {'aus': 7259, 'eng': 3577, 'pak': 8632, 'sri lanka': 5456}

sports = ['cricket', 'tennis', 'soccer', 'boxing', 'swimming']

def greet(pname):
    print(f"Greetings Mr. {pname}, Welcome to the event....")

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.age}"

