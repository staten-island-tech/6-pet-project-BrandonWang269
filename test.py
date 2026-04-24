""" class calculator():
    def add(x,y):
        print(x + y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)
    def subtract(numbers):
        return numbers
calculator.add(5,11) """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jullian = Hero("Jullian", 150, ["Potion"])
Jullian.buy({"title": "Sword", "atk": 34})
print(Jullian.__dict__)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}") """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Cipher = Hero("Cipher", 1000, ["Wand"])
Cipher.buy({"title": "Hat", "def": 67})
print(Cipher.__dict__) """

class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, increase):
        self.__happiness += increase
    def show_status(self):
        print(f"{self.name} has {self.__happiness} happiness")

Carson = Pet("Carson", 0)
Carson.play(15)
Carson.show_status()