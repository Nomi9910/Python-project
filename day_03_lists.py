"""
=============================================================
 Day 3 - Lists
=============================================================
 A list is an ordered, mutable collection of items.
 Lists can hold mixed types and allow duplicates.
 Indexed from 0. Support slicing, appending, and more.
=============================================================
"""

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])   # First element
print(fruits[-1])  # Last element

# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[::2])   # Every other: [0, 2, 4]

# Modifying
fruits[1] = "blueberry"
print(fruits)

# Adding elements
fruits.append("mango")        # Add to end
fruits.insert(1, "avocado")   # Insert at index
print(fruits)

# Removing elements
fruits.remove("cherry")       # Remove by value
popped = fruits.pop()         # Remove last
print(f"Popped: {popped} | List: {fruits}")

# Useful methods
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Length : {len(nums)}")
print(f"Min    : {min(nums)}")
print(f"Max    : {max(nums)}")
print(f"Sum    : {sum(nums)}")
print(f"Sorted : {sorted(nums)}")
print(f"Count 1: {nums.count(1)}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")
