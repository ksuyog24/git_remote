# Task: Defining Functions

# 1. Define a function that prints a message twice
def displayTwice(msg):
    """
    Prints the provided message twice to the screen.
    """
    print(msg)
    print(msg)

# Test the function
print("--- Testing displayTwice ---")
displayTwice("Hello World")
displayTwice("Python is fun")

# 2. Check the docstring (prints the documentation we wrote above)
print("\n--- Testing Docstring ---")
help(displayTwice)

# 3. Define a function that returns a value (Max of two numbers)
def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        return a
    else:
        return b

# Test the return value
print("\n--- Testing findMax ---")
print("Max of 10 and 5 is:", findMax(10, 5))
print("Max of 3 and 99 is:", findMax(3, 99))