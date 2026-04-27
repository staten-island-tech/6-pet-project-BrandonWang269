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

""" class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, increase):
        self.__happiness += increase
    def show_status(self):
        print("Bob is playing fetch!")
        print(f"{self.name} has {self.__happiness} happiness")

Bob = Pet("Bob", 0)
Bob.play(15)
Bob.show_status() """

""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item, cost):
        self.inventory.append(item)
        self.money -= cost
        print(self.inventory)

Cipher = Hero("Cipher", 1000, ["Wand"])
Cipher.buy({"title": "Hat", "def": 67,}, 232)
print(Cipher.__dict__) """

""" class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"

class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system."
    

student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())
print(teacher.display_info()) 
print(administrator.display_info()) 

admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())
my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info()) """

class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness
    def play(self, increase):
        self.__happiness += increase
    def show_status(self):
        print("Bob is playing fetch!")
        print(f"{self.name} has {self.__happiness} happiness")

Bob = Pet("Bob", 0)
Bob.play(15)
Bob.show_status()