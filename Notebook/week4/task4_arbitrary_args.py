# Task: Arbitrary Length Argument Lists

# Define a function that takes any number of arguments
def calcAve(*numbers):
    total = 0
    # Loop through the tuple of numbers
    for num in numbers:
        total += num
    
    # Avoid division by zero
    if len(numbers) == 0:
        return 0
        
    return total / len(numbers)

print("--- Testing calcAve ---")
# Test with 3 numbers
print("Average of 10, 20, 30 is:", calcAve(10, 20, 30))

# Test with 2 numbers
print("Average of 5, 5 is:", calcAve(5, 5))

# Test with 5 numbers
print("Average of 1, 2, 3, 4, 5 is:", calcAve(1, 2, 3, 4, 5))