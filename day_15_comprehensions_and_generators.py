"""
=============================================================
 Day 15 - List Comprehensions & Generators
=============================================================
 Comprehensions are concise, readable ways to build
 collections (list, dict, set) from iterables.
 Generators produce items one at a time — memory efficient
 for large datasets. Use () instead of [] for generator exprs.
=============================================================
"""

# ── List comprehension ────────────────────────────────────
# [expression for item in iterable if condition]

squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

words = ["hello", "world", "python", "rocks"]
upper = [w.upper() for w in words if len(w) > 4]
print("Upper long words:", upper)

# Nested list comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flat:", flat)

# ── Dict comprehension ────────────────────────────────────
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

squared_dict = {x: x**2 for x in range(1, 6)}
print("Squared dict:", squared_dict)

# ── Set comprehension ─────────────────────────────────────
unique_lengths = {len(word) for word in words}
print("Unique lengths:", unique_lengths)

# ── Generator expression ──────────────────────────────────
# Like list comprehension but uses () — lazy evaluation
gen = (x**2 for x in range(1, 6))
print("Generator:", gen)
print("Next:", next(gen))
print("Next:", next(gen))
print("Rest:", list(gen))

# ── Generator function ────────────────────────────────────
def countdown(n):
    while n > 0:
        yield n    # pauses here and returns n
        n -= 1

for val in countdown(5):
    print(val, end=" ")
print()

# Infinite generator — safe because it's lazy
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

counter = infinite_counter(10)
print([next(counter) for _ in range(5)])  # [10,11,12,13,14]

# ── Memory comparison ─────────────────────────────────────
import sys

list_comp = [x**2 for x in range(10000)]
gen_expr  = (x**2 for x in range(10000))

print(f"List size    : {sys.getsizeof(list_comp):,} bytes")
print(f"Generator sz : {sys.getsizeof(gen_expr):,} bytes")
print("Generators win on memory for large data!")
