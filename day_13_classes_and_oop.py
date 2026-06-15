"""
=============================================================
 Day 13 - Classes & Object-Oriented Programming (OOP)
=============================================================
 OOP organizes code into objects that bundle data (attributes)
 and behaviour (methods). Key concepts:
 - Class    : blueprint for objects
 - Object   : instance of a class
 - __init__ : constructor (runs on object creation)
 - self     : refers to the current instance
=============================================================
"""

# ── Basic class ───────────────────────────────────────────
class Dog:
    species = "Canis familiaris"   # class attribute (shared)

    def __init__(self, name, age):
        self.name = name           # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2)
print(Dog.species)

# ── Inheritance ───────────────────────────────────────────
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"

animals = [Cat("Whiskers"), Duck("Donald"), Dog("Rex", 2)]
for animal in animals:
    print(animal.speak())

# ── Encapsulation ─────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: ${acc.get_balance()}")

# ── Class & static methods ────────────────────────────────
class MathHelper:
    pi = 3.14159

    @classmethod
    def circle_area(cls, r):
        return cls.pi * r ** 2

    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.circle_area(5))
print(MathHelper.add(3, 4))
