"""
=============================================================
 Day 4 - Tuples
=============================================================
 A tuple is an ordered, IMMUTABLE collection of items.
 Once created, elements cannot be added, changed, or removed.
 Tuples are faster than lists and used for fixed data.
=============================================================
"""

# Creating tuples
coordinates = (10.5, 20.3)
rgb = (255, 128, 0)
single = (42,)          # Comma required for single-element tuple
empty = ()

print(coordinates, rgb, single, empty)

# Accessing elements
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Slicing (same as lists)
nums = (0, 1, 2, 3, 4)
print(nums[1:3])   # (1, 2)

# Tuple unpacking — very powerful
name, age, city = ("Alice", 30, "New York")
print(f"{name} is {age} from {city}")

# Swap using tuple unpacking
a, b = 5, 10
a, b = b, a
print(f"a={a}, b={b}")

# Useful methods
colors = ("red", "blue", "red", "green")
print(f"Count 'red': {colors.count('red')}")
print(f"Index 'blue': {colors.index('blue')}")
print(f"Length: {len(colors)}")

# Convert between list and tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(my_tuple, back_to_list)

# Tuples as dictionary keys (lists cannot be used as keys)
location_data = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}
print(location_data[(40.7128, -74.0060)])
