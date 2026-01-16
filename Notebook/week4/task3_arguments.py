# Task: Default and Keyword Arguments

# 1. Function with Default Arguments
# If 'b' is missing, it should multiply 'a' by itself.
def custom_multiply(a, b=None):
    if b is None:
        return a * a  # Square the number
    else:
        return a * b  # Multiply normally

print("--- Testing Default Arguments ---")
print("5 * 3 =", custom_multiply(5, 3))
print("4 squared =", custom_multiply(4))  # Missing second argument

# 2. Keyword Arguments
def showMsg(title, body="", prefix="INFO", suffix="."):
    print(prefix, title, body, suffix)

print("\n--- Testing Keyword Arguments ---")
# Call using keywords in different orders
showMsg(title="File Error", prefix="ERROR")
showMsg(prefix="WARNING", title="Disk Full", body="Please delete files")

# 3. Built-in keyword argument example
print("\n--- Testing print() separator ---")
print("192", "168", "0", "1", sep=".")