# Introduction to Programming – Complete Portfolio

This repository serves as the comprehensive submission for the *Introduction to Programming* module. It contains the **Final Assessment Tasks**, the **Weekly Python Source Code**, and the **Weekly Logbooks** documenting my theoretical understanding.

---

## Part 1: Final Assessment Tasks

This section contains the solutions for **Task 1** and **Task 2**. These scripts demonstrate fundamental concepts like input validation, loops, conditional statements, and algorithm design.

### **Task 1: Beckett Pizza Plaza**
* **File:** `task1.py`
* **Description:** A script handling a **4-for-3 promotion deal**. It calculates the total order cost by identifying the cheapest pizza and removing it as a discount.

#### **Key Implementation Details**
* **Input & Validation:** Uses a `while` loop and `try-except` blocks to ensure only positive numbers are accepted.
* **Logic:** Stores prices in a list, uses `min()` to find the lowest value, and `sum()` to calculate the subtotal.
* **Rules Applied:**
    * The maximum discount achievable is **25%** (when all pizzas are equal price).
    * The program enforces exactly four pizza inputs.
* **Output:** formats currency and discount percentages to 2 decimal places.

### **Task 2: Password Security Check**
* **File:** `task2.py`
* **Description:** A security simulation mimicking **Partial Password Authentication**, a technique commonly used in banking to prevent credential theft.

#### **Key Implementation Details**
* **Validation:** Checks that the password is at least **9 characters long** using `len()`.
* **Randomization:** Uses `random.randint()` to generate three random indices to test the user.
* **Security Logic:** If any character is incorrect, the program halts immediately using `return`.
* **Rules Applied:**
    * Random positions can repeat (the system may ask for the same index twice).
    * Immediate termination on failure.

---

## Part 2: Weekly Code Portfolio

This section contains the **Python source code (`.py`)** developed during the weekly laboratory sessions (Weeks 1–8).

* **Week 1 (`week1.py`): Basics & Environment**
    * Introduction to the Python Interpreter, arithmetic operators, and handling syntax vs. runtime errors.
* **Week 2 (`week2.py`): Variables & Lists**
    * Variable assignment, dynamic typing, and manipulating mutable lists vs. immutable strings.
* **Week 3 (`week3.py`): Control Flow**
    * Logic control using `if/elif/else`, boolean expressions, and iteration with `while` and `for` loops.
* **Week 4 (`week4/`): Functions & Modules**
    * Defining functions with `def`, using `return`, default arguments, `*args`, and lambda expressions.
* **Week 5 (`week5.py`): Scripts & Command Line**
    * Processing command line arguments (`sys.argv`) and understanding the `if __name__ == "__main__":` block.
* **Week 6 (`week6.py`): Advanced Lists**
    * List comprehensions, list methods (`.append()`, `.pop()`), and tuple unpacking.
* **Week 7 (`week 7.py`): Sets & Dictionaries**
    * Working with unordered `sets` and key-value `dictionaries` to manage data efficiently.
* **Week 8 (`week8.py`): File I/O**
    * Reading and writing text files, and using **f-strings** for advanced output formatting.

---

## Part 3: Weekly Logbooks

This section contains the **Weekly Logbooks (`.docx`)**. These documents cover the theoretical aspects of the module, including answers to lecture questions and definitions of key terminology.

* **Week 1:** Machine Code vs. High-Level Languages, Interpreter vs. Compiler.
* **Week 2:** Data types (`int`, `float`, `str`), Mutability, and variable naming conventions.
* **Week 4:** Function parameters, return values, and modular programming concepts.
* **Week 5:** Script execution modes and the module search path (`sys.path`).
* **Week 6:** Heterogeneous vs. Homogeneous sequences, Method calls vs. Function calls.
* **Week 7:** Set theory (Union/Intersection) and Dictionary hashing concepts.
* **Week 8:** File pointers (`seek`, `tell`) and safe file handling with the `with` statement.

---

##  Technologies Used
* **Language:** Python 3.x
* **Editor:** VS Code 
* **Documentation:** Microsoft Word

## How to Run the Programs
Ensure Python 3 is installed. Open a terminal, navigate to the folder, and run the desired file:

```bash
# Run the Final Tasks
python task1.py
python task2.py

# Run a Weekly Script
python week1.py