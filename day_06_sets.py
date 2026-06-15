"""
=============================================================
 Day 6 - Sets
=============================================================
 A set is an unordered collection of UNIQUE items.
 No duplicates allowed. Unindexed — no positional access.
 Ideal for membership tests and mathematical set operations.
=============================================================
"""

# Creating sets
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate removed
print(fruits)  # order is not guaranteed

empty_set = set()  # NOT {} — that creates an empty dict!

# Adding / removing
fruits.add("mango")
fruits.discard("banana")     # No error if not found
fruits.remove("cherry")      # Raises error if not found
print(fruits)

# Membership test (very fast — O(1))
print("apple" in fruits)
print("grape" not in fruits)

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Union       : {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference  : {a - b}")
print(f"Sym. Diff   : {a ^ b}")

# Subset / superset
x = {1, 2}
print(x.issubset(a))    # True
print(a.issuperset(x))  # True

# Remove duplicates from a list
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique = list(set(names))
print(unique)

# Frozenset (immutable set — can be used as dict key)
immutable = frozenset([1, 2, 3])
print(immutable)
