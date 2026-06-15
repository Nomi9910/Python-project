"""
=============================================================
 Day 10 - String Methods
=============================================================
 Strings are immutable sequences of characters.
 Python provides many built-in methods to manipulate them.
 String methods always return a NEW string — originals unchanged.
=============================================================
"""

text = "  Hello, Python World!  "

# Case methods
print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())

# Strip whitespace
print(text.strip())    # both ends
print(text.lstrip())   # left only
print(text.rstrip())   # right only

# Find & replace
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.find("fox"))         # index of first occurrence
print(sentence.count("the"))        # case-sensitive count
print(sentence.replace("fox", "cat"))

# Split & join
csv = "alice,bob,charlie,dave"
names = csv.split(",")
print(names)
print(" | ".join(names))

words = sentence.split()
print(words[:3])

# Check content
print("12345".isdigit())
print("hello".isalpha())
print("hello123".isalnum())
print("  ".isspace())
print(sentence.startswith("The"))
print(sentence.endswith("dog"))

# Formatting
name = "Alice"
age = 30
# f-string (recommended)
print(f"Name: {name}, Age: {age}")
# .format()
print("Name: {}, Age: {}".format(name, age))
# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))

# Padding and alignment
print(f"{'left':<10}|")
print(f"{'right':>10}|")
print(f"{'center':^10}|")
print(f"{3.14159:.2f}")
print(f"{1000000:,}")

# Multiline string
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you!"""
print(poem)
