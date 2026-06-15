"""
=============================================================
 Day 14 - Modules & Imports
=============================================================
 A module is a .py file containing reusable code.
 Python has a huge standard library — math, os, sys,
 datetime, random, json, re, and many more built-in modules.
 Install third-party modules with: pip install <name>
=============================================================
"""

# ── math module ───────────────────────────────────────────
import math

print(math.pi)
print(math.e)
print(math.sqrt(144))
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.factorial(6))
print(math.log(100, 10))

# ── random module ─────────────────────────────────────────
import random

print(random.random())             # float between 0 and 1
print(random.randint(1, 100))      # random integer
print(random.choice(["a", "b", "c"]))
nums = list(range(10))
random.shuffle(nums)
print(nums)
print(random.sample(nums, 3))

# ── datetime module ───────────────────────────────────────
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.year, now.month, now.day)

tomorrow = date.today() + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# ── os module ─────────────────────────────────────────────
import os

print(os.getcwd())
print(os.getenv("PATH", "not set")[:50])
print(os.path.join("home", "user", "docs"))

# ── sys module ────────────────────────────────────────────
import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# ── json module ───────────────────────────────────────────
import json

data = {"name": "Alice", "age": 30, "skills": ["Python", "Linux"]}

json_str = json.dumps(data, indent=2)   # dict -> JSON string
print(json_str)

parsed = json.loads(json_str)           # JSON string -> dict
print(parsed["skills"])

# ── Selective imports ─────────────────────────────────────
from math import sqrt, pi
from os.path import exists, join

print(sqrt(81))
print(pi)

# ── Aliased import ────────────────────────────────────────
import datetime as dt
print(dt.date.today())
