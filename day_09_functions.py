"""
=============================================================
 Day 9 - Functions
=============================================================
 Functions are reusable blocks of code defined with `def`.
 They can accept parameters and return values.
 Good functions do ONE thing and do it well.
=============================================================
"""

# Basic function
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9  (uses default exponent=2)
print(power(2, 10))  # 1024

# Keyword arguments
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}.")

describe_pet(animal="cat", name="Whiskers")

# Multiple return values (returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")

# *args — variable number of positional arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))  # 15

# **kwargs — variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Bob", age=25, city="NYC")

# Lambda — anonymous one-liner function
square = lambda x: x ** 2
print(square(7))

nums = [5, 2, 8, 1, 9]
print(sorted(nums, key=lambda x: -x))  # descending

# Docstring
def multiply(a, b):
    """Return the product of a and b."""
    return a * b

print(multiply.__doc__)
