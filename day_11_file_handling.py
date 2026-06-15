"""
=============================================================
 Day 11 - File Handling
=============================================================
 Python can read from and write to files using open().
 Always use `with` statement — it auto-closes the file.
 Modes: 'r' read | 'w' write | 'a' append | 'b' binary
=============================================================
"""
import os

# ── Writing to a file ──────────────────────────────────────
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello, File!\n")
    f.write("Line 2: Python file handling is easy.\n")
    f.write("Line 3: Always use the 'with' statement.\n")

print("File written successfully.")

# ── Reading entire file ────────────────────────────────────
with open("sample.txt", "r") as f:
    content = f.read()
    print("Full content:\n", content)

# ── Reading line by line ───────────────────────────────────
with open("sample.txt", "r") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"  [{line_num}] {line.strip()}")

# ── Reading all lines into a list ─────────────────────────
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")

# ── Appending to a file ────────────────────────────────────
with open("sample.txt", "a") as f:
    f.write("Line 4: Appended line!\n")

# ── Check if file exists ───────────────────────────────────
print(os.path.exists("sample.txt"))   # True
print(os.path.getsize("sample.txt"))  # size in bytes

# ── Rename and delete ──────────────────────────────────────
os.rename("sample.txt", "renamed.txt")
print(os.path.exists("renamed.txt"))  # True
os.remove("renamed.txt")
print(os.path.exists("renamed.txt"))  # False

# ── Working with directories ───────────────────────────────
os.makedirs("test_dir/sub_dir", exist_ok=True)
print(os.listdir("."))
os.removedirs("test_dir/sub_dir")
