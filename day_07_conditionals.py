"""
=============================================================
 Day 7 - Conditionals (if / elif / else)
=============================================================
 Conditionals let your program make decisions.
 Python uses indentation (4 spaces) to define code blocks.
 Comparison: ==  !=  >  <  >=  <=
 Logical:    and  or  not
=============================================================
"""

# Basic if / elif / else
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} | Grade: {grade}")

# Logical operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")

# not operator
is_raining = False
if not is_raining:
    print("Go outside!")

# Nested conditionals
num = -5
if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")

# Ternary (one-liner) conditional
x = 10
label = "even" if x % 2 == 0 else "odd"
print(f"{x} is {label}")

# Checking membership
role = "admin"
if role in ("admin", "superuser"):
    print("Full access")
else:
    print("Limited access")

# Truthy / falsy values
for val in [0, "", None, [], False, 1, "hello", [1], True]:
    print(f"{str(val):10} -> {'Truthy' if val else 'Falsy'}")
