import datetime

print("Hello from my Python app!")
print("Current time:", datetime.datetime.now().isoformat())

# Simple function
def add(a, b):
    return a + b

print("2 + 3 =", add(2, 3))

# Show Python version
import sys
print("Python version:", sys.version)