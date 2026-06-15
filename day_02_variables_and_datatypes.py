"""
=============================================================
 Day 2 - Variables & Data Types
=============================================================
 Variables store data values. Python is dynamically typed —
 you don't need to declare a type; Python figures it out.
 Core data types: int, float, str, bool, NoneType
=============================================================
"""

# Integer
age = 25
print(f"Integer: {age} | Type: {type(age)}")

# Float
price = 19.99
print(f"Float: {price} | Type: {type(price)}")

# String
name = "Bob"
print(f"String: {name} | Type: {type(name)}")

# Boolean
is_active = True
print(f"Boolean: {is_active} | Type: {type(is_active)}")

# NoneType (absence of value)
result = None
print(f"NoneType: {result} | Type: {type(result)}")

# Type conversion
num_str = "100"
num_int = int(num_str)       # str -> int
num_float = float(num_str)   # str -> float
print(f"Converted int: {num_int}, float: {num_float}")

# Multiple assignment
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# Swap values
a, b = 10, 20
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Check type
print(isinstance(age, int))   # True
print(isinstance(name, str))  # True
