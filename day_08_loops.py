"""
=============================================================
 Day 8 - Loops (for & while)
=============================================================
 Loops repeat a block of code multiple times.
 for  : iterate over a sequence (list, range, string, etc.)
 while: repeat as long as a condition is True
 Control: break (exit), continue (skip), else (on completion)
=============================================================
"""

# for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with range()
for i in range(5):       # 0 to 4
    print(i, end=" ")
print()

for i in range(1, 10, 2):   # 1,3,5,7,9
    print(i, end=" ")
print()

# Enumerate — get index + value
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# Zip — iterate two lists together
names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# while loop
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# break — exit loop early
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")
print()

# continue — skip current iteration
for n in range(10):
    if n % 2 == 0:
        continue
    print(n, end=" ")  # prints odd numbers only
print()

# else on a for loop (runs if loop completes without break)
for n in range(5):
    print(n, end=" ")
else:
    print("\nLoop completed!")

# Nested loops — multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()
