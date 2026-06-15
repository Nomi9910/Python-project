"""
=============================================================
 Day 12 - Exception Handling
=============================================================
 Exceptions are runtime errors. Handle them gracefully with
 try / except / else / finally blocks so your program does
 not crash unexpectedly.
=============================================================
"""

# Basic try / except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Catching multiple exceptions
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer.")
    except TypeError:
        print("Wrong type provided.")
    return None

print(safe_convert("42"))    # 42
print(safe_convert("abc"))   # error message
print(safe_convert(None))    # error message

# else — runs if NO exception occurred
try:
    num = int("100")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion succeeded: {num}")

# finally — always runs (cleanup code)
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs — great for cleanup.")

# Catching the exception object
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError caught: {e}")

# Raise your own exception
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}. Must be between 0 and 150.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)

# Custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    new_balance = withdraw(100, 250)
except InsufficientFundsError as e:
    print(e)
