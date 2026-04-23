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

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jullian = Hero("Julloan", 150, ["Potion"])
Jullian.buy({"title": "Sword", "atk": 34})
print(Jullian.__dict__)