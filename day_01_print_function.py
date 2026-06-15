"""
=============================================================
 Day 1 - The print() Function
=============================================================
 The print() function outputs text or values to the screen.
 It is the most basic way to display information in Python.
 You can print strings, numbers, variables, or expressions.
=============================================================
"""

# Basic string output
print("Hello, World!")

# Printing numbers
print(42)
print(3.14)

# Printing multiple values (separated by space by default)
print("Python", "is", "awesome")

# Custom separator
print("2024", "06", "15", sep="-")

# Custom end character (default is newline \n)
print("Hello", end=" ")
print("World!")

# Printing variables
name = "Alice"
age = 30
print("Name:", name, "| Age:", age)

# Using f-strings (modern and recommended)
print(f"My name is {name} and I am {age} years old.")

# Printing expressions
print(f"2 + 2 = {2 + 2}")
