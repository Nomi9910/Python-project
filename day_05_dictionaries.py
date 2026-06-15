"""
=============================================================
 Day 5 - Dictionaries
=============================================================
 A dictionary stores key-value pairs. Keys must be unique
 and immutable (strings, numbers, tuples). Values can be
 anything. Ordered (Python 3.7+) and mutable.
=============================================================
"""

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing values
print(person["name"])
print(person.get("age"))
print(person.get("email", "Not found"))  # Default value

# Adding / updating
person["email"] = "alice@example.com"
person["age"] = 31
print(person)

# Deleting
del person["city"]
removed = person.pop("email")
print(f"Removed: {removed} | Dict: {person}")

# Iterating
student = {"math": 95, "english": 88, "science": 92}

for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"  {key} -> {value}")

# Keys, values, items
print(list(student.keys()))
print(list(student.values()))

# Nested dictionaries
users = {
    "user1": {"name": "Bob", "role": "admin"},
    "user2": {"name": "Eve", "role": "viewer"},
}
print(users["user1"]["role"])

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Merging dicts (Python 3.9+)
defaults = {"theme": "dark", "lang": "en"}
user_prefs = {"lang": "fr"}
merged = {**defaults, **user_prefs}
print(merged)
