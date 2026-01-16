# ==========================================
# TASK 2: PASSWORD SECURITY CHECK
# ==========================================
import random

def password_security_check():
    """
    This function prompts the user for a password,
    checks if it meets the minimum length requirement,
    and verifies 3 random letters from the password.
    """
    # Ask the user to enter their password
    pwd = input("Enter your password: ")

    # Check if password length is sufficient
    if len(pwd) < 9:
        print("Password too short. Must be at least 9 characters.")
        return  

    print("Password length is sufficient.")
    print("You will now be asked for 3 letters from your password.")

    # Loop to verify 3 random letters
    for i in range(3):
        pos = random.randint(1, len(pwd))

        user_letter = input(f"Enter letter at position {pos}: ")

        if user_letter == pwd[pos - 1]:
            print("Correct")
        else:
            print("Security check failed.")
            return 

    # If loop finishes without returning, all letters were correct
    print("Security check passed. You have successfully entered the password!")

if __name__ == "__main__":
    password_security_check()