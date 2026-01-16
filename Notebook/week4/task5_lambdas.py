# Task: Lambda Expressions
import math

# 1. Simple Lambda (Hypotenuse)
hypot = lambda a, b: math.sqrt(a * a + b * b)

print("--- Testing Hypot Lambda ---")
print("Hypotenuse of 3 and 4 is:", hypot(3, 4))
print("Type of hypot variable is:", type(hypot))

# 2. Lambda to calculate seconds

to_seconds = lambda hours, minutes=0: (hours * 3600) + (minutes * 60)

print("\n--- Testing to_seconds Lambda ---")
print("0 hrs, 2 mins =", to_seconds(0, 2))
print("2 hrs, 0 mins =", to_seconds(2, 0))
print("1 hr, 30 mins =", to_seconds(1, 30))

# Testing the default argument (only passing hours)
print("1 hr (default 0 mins) =", to_seconds(1))
print("2 hrs (default 0 mins) =", to_seconds(2))