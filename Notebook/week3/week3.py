# Week 3 – Introduction to Programming Exercises
# Name: Suyog Khadka 
# Date: 28/11/2025

# --- Boolean Expressions ---
print("Boolean Expressions Examples:")
print(10 < 100)        
print(100 != 100)      
print(50 >= 50)        

# Using a variable
age = 25
print(age < 18)        
print(age < 21)       
print(age < 31)        

# Comparing strings
print("a" < "b")       
print("b" < "a")       
print("John" < "Terry")
print("john" < "Terry")

# --- Logical Operators ---
age = 30
print(age >= 18 and age <= 65) 
print(age < 18 or age > 65)    
print(not age > 18)            

# Combining logical operators
print((age >= 18 and age <= 65) and (not age == 30))  

# Chaining relational operators
weight = 150
height = 150
print(100 < weight < 200)       
print(131 < height < 160)       

# --- Membership Testing ---
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("Eric" in names)          
print("Mark" not in names)      

message = "Hello there, my name is John"
print("nam" in message)         

# --- If / Else / Elif Statements ---
age = 25
if 18 <= age <= 30:
    print("You are still young!")

# If-elif-else with multiple conditions
age = 35
if age > 100:
    print("You are very old, well done!")
elif age > 80:
    print("You are fairly old, pretty good!")
elif age > 40:
    print("You are middle aged, never mind")
elif age > 30:
    print("You are in your early thirties!")
else:
    print("You are not very old - yet")

# Non-boolean conditions
total = 10
if total != 0:
    print("Total is non-zero")
else:
    print("Total is zero")

name = input("Enter your name: ")
if bool(name):
    print("Your name is", name)
else:
    print("Name not entered")

# --- Ternary Operator ---
age = 20
print("You are an adult" if age >= 18 else "You are not an adult, yet!")

# --- While Loop ---
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1

# --- For Loop with a list ---
names = ["Alice", "Bob", "Charlie", "David"]
for n in names:
    print("Name:", n)

# --- For Loop with range() ---
for n in range(2, 12, 2):  # 2,4,6,8,10
    print(f"{n} to the power of {n} = {n**n}")

# --- For Loop with break ---
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    if num > 100:
        print("Number over 100 found, breaking loop!")
        break
    total += num
    print("Running total:", total)
else:
    print("All numbers processed")

# --- For Loop with continue ---
grades = [20, 50, 43, 33, 90, 15]
pass_mark = 40
passes = 0
total_passes = 0
for grade in grades:
    if grade < pass_mark:
        continue
    passes += 1
    total_passes += grade
print("Average pass mark was:", total_passes / passes)