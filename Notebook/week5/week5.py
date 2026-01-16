import sys

# ==============================================================================
# SECTION 1: MODULE DEFINITIONS (Task: my_utils.py)
# ==============================================================================

# The worksheet asks for an initialisation statement that prints when imported
print("Welcome, utils module has been imported and initialised!")

def average(values):
    """ Calculates the average of the given list. """
    # This function is from the 'Writing Modules' section
    total = 0
    for n in values:        # total the given values
        total += float(n)       
    
    if len(values) == 0:
        return 0
    return total / len(values)  # return calculated average


# ==============================================================================
# SECTION 2: MAIN SCRIPT EXECUTION
# ==============================================================================
if __name__ == "__main__":
    
    print("\n" + "="*50)
    print("TASK: show_path.py (Module Search Path)")
    print("="*50)
    # Task: Print the sys.path variable
    print("The import search path for this program is:", sys.path)

    
    print("\n" + "="*50)
    print("TASK: first_prog.py (Interactive Input & Logic)")
    print("="*50)
    
    # Task: Add comments above each statement describing what it does.
    
    # Prompt the user to input a string from the console
    number_input = input("Enter a number: ")

    try:
        # Convert the string input into an integer type
        number = int(number_input)

        # Print the converted number back to the user
        print("The number entered was", number)

        # Check if the number is even using the modulo operator
        if (number % 2) == 0:
            # If remainder is 0, print that it is even
            print("That is an even number")
        else:
            # If remainder is not 0, print that it is odd
            print("That is an odd number")

        # Task: Add extra code to identify if divisible by 10
        # Check if the number is divisible by 10
        if (number % 10) == 0:
            print("That is divisible by 10")
        else:
            print("That is not divisible by 10")

    except ValueError:
        print("Error: The value entered was not a valid integer.")


    print("\n" + "="*50)
    print("TASK: total.py (Command Line Arguments & Summation)")
    print("="*50)

    # Task: Check if no arguments have been passed
    # We check if len is 1 because sys.argv[0] is the script name itself
    if len(sys.argv) == 1:
        print("No arguments were provided.")
    else:
        # Task: Use the specific WHILE loop logic provided in the worksheet
        count = len(sys.argv)
        total = 0
        
        # Note: This loop works backwards from the end of the list down to index 1
        while count > 1:
            count -= 1
            # Convert argument to float and add to total
            total += float(sys.argv[count])

        print("Total is", total)
        
        # Task: Calculate and print the average (improving total.py)
        # We subtract 1 from len(sys.argv) to ignore the filename
        num_values = len(sys.argv) - 1
        avg = total / num_values
        print("Average (calculated in main loop) is", avg)


    print("\n" + "="*50)
    print("TASK: my_utils.py (Using the Module Function)")
    print("="*50)
    
    if len(sys.argv) > 1:
        # We pass the arguments (excluding the script name) to the function
        # defined at the top of this file.
        args = sys.argv[1:]
        result = average(args)
        print("Average (calculated via function) is", result)
    else:
        print("No arguments provided, so average function was not called.")