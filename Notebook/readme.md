# Introduction to Programming – Weekly Code Portfolio

This repository contains the **Python source code solutions** for the practical laboratory exercises (Weeks 1–8). These scripts demonstrate the progression from basic syntax to complex file handling and data structure manipulation.

---

## Repository Structure & Content

### **Week 1: Basics & Environment**
* **File:** `week1.py`
* **Description:** An introduction to the Python environment and basic arithmetic.
* **Key Features:**
  * Outputting text using `print()`.
  * Mathematical operators (`+`, `-`, `*`, `/`, `//`, `**`, `%`).
  * Handling **Operator Precedence** (PEMDAS).
  * Error handling examples: **Syntax Errors** vs. **ZeroDivisionError** (Runtime).

### **Week 2: Variables & Lists**
* **File:** `week2.py`
* **Description:** Manipulation of variables and introduction to mutable sequences.
* **Key Features:**
  * **Augmented Assignment** operators (`+=`, `-=`, `*=`).
  * Dynamic typing checks using `type()`.
  * **List Slicing** (e.g., `primes[0:4]`) and indexing.
  * demonstrating **Mutability** (Lists) vs. **Immutability** (Strings).

### **Week 3: Control Flow**
* **File:** `week3.py`
* **Description:** Logic control using conditionals and loops.
* **Key Features:**
  * **Boolean Expressions** and Relational Operators (`<`, `!=`, `==`).
  * Logical Operators (`and`, `or`, `not`).
  * `if`, `elif`, `else` blocks for decision making.
  * **Ternary Operator** usage.
  * Iteration using `while` loops and `for` loops (including `range()`).

### **Week 4: Functions & Modules**
* **Directory:** `week4/`
* **Description:** Breakdown of function mechanics and library usage.
  * `task1_imports.py`: Importing standard libraries (`math`, `math.sqrt`, `math.log2`).
  * `task2_defining_functions.py`: Defining functions using `def`, returning values, and using **Docstrings**.
  * `task3_arguments.py`: Implementing **Default Arguments** (`b=None`) and **Keyword Arguments**.
  * `task4_arbitrary_args.py`: Handling variable numbers of arguments using `*args`.
  * `task5_lambdas.py`: Writing anonymous **Lambda functions** for concise logic.

### **Week 5: Scripts & Command Line Arguments**
* **File:** `week5.py`
* **Description:** Working with system arguments and script modularity.
* **Key Features:**
  * Importing the `sys` module to access `sys.argv`.
  * Processing **Command Line Arguments** to calculate totals and averages.
  * Using the `if __name__ == "__main__":` block to make code importable.
  * Inspecting the Module Search Path (`sys.path`).

### **Week 6: Advanced Lists & Tuples**
* **File:** `week6.py`
* **Description:** Advanced sequence manipulation.
* **Key Features:**
  * **List Methods:** `.append()`, `.extend()`, `.insert()`, `.remove()`, `.sort()`.
  * **List Comprehensions:** Concise generation of lists (e.g., `[x**3 for x in range(2, 21)]`).
  * **Tuples:** Creation, single-element tuples, and **Tuple Unpacking** (`a, b, c = coord`).

### **Week 7: Sets & Dictionaries**
* **File:** `week 7.py`
* **Description:** Working with unordered collections and key-value pairs.
* **Key Features:**
  * **Sets:** Creation, membership testing (`in`), and set theory operations (Union `|`, Intersection `&`).
  * **Frozensets:** Immutable set implementation.
  * **Dictionaries:** Key-value storage, adding items, and iterating over keys/values.
  * **Set & Dictionary Comprehensions**.

### **Week 8: File I/O & Formatting**
* **File:** `week8.py`
* **Description:** Reading/Writing files and advanced string formatting.
* **Key Features:**
  * **f-strings:** Advanced formatting for alignment (`:>20`), padding, and precision (`:.2f`).
  * **File Writing:** Creating and writing to `info.txt`.
  * **File Reading:** Reading entire content, line-by-line referencing, and looping over file objects.

---

## Technologies Used
**Language:** Python 3.x (CPython Interpreter)
* **Environment:** VS Code 
* **Standard Libraries:** `math`, `sys`, `random`

---

## How to Run the Code

Ensure you have Python 3 installed. You can run individual week scripts from your terminal:

```bash
# Run a specific week (e.g., Week 1)
python week1.py

# Run Week 5 (Example with arguments)
python week5.py 10 20 30

# Run Week 4 Tasks (Navigate to folder first)
cd week4
python task1_imports.py