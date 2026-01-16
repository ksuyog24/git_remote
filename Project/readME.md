# Introduction to Programming – Final Assignment

This repository contains the solutions for **Task 1** and **Task 2** of the final assignment. Both tasks are implemented in Python and emphasize fundamental programming concepts like input validation, loops, conditional statements, and basic computations.

---

## Task 1: Beckett Pizza Plaza
### Description
This script handles a **4-for-3 promotion deal**. It computes the order total by identifying the least expensive pizza and deducting it as a discount. The customer must order exactly four pizzas, and the cheapest pizza is free.

### The Program
* **Input:** Prompts the user to enter the price of exactly four pizzas.
* **Validation:** Uses a `while` loop and `try-except` blocks to ensure only positive numbers are accepted.
* **Logic:** Stores prices in a list, uses `min()` to find the cheapest item, and `sum()` to calculate the subtotal.
* **Output:** Displays the total payable and the discount percentage formatted to 2 decimal places.

### Rules Applied
* Pizza prices must be greater than zero.
* Discount computation is based on the percentage of the total order.
* The **maximum discount achievable is 25%** (when all pizzas are equal price).
* The program is set to accept exactly four pizza prices.

### What I Learned
* Using **loops** to ensure exactly four valid inputs.
* Storing multiple values using a **List**.
* Locating the lowest value with `min()` and computing totals using `sum()`.
* Implementing conditional logic using `if/else` blocks.
* Transforming real-world problems into **Input → Validation → Calculation → Output** steps.

---

## Task 2: Password Security Check
### Description
A security simulation that mimics **Partial Password Authentication**, a technique commonly used by banking applications to prevent credential theft.

### The Program
1. **Step 1:** Prompts the user to enter a password.
2. **Step 2:** Checks that the password is at least **9 characters long** using `len()`.
3. **Step 3:** Uses `random.randint()` to generate three random positions to test the user.
4. **Step 4:** If any character is incorrect, the program stops immediately using `return`.

### Rules Applied
* Passwords under 9 characters are rejected.
* Random positions can repeat (the system may ask for the same character index twice).
* The program uses `return` to terminate the function immediately upon failure.

### What I Learned
* Determining string length using `len()`.
* Retrieving specific characters via **Indexing** (e.g., `pwd[index]`).
* Using `random.randint()` to generate test cases.
* Halting program execution instantly with `return`.
* Developing basic password security validation flows.

---

## Technologies Used
* **Python 3**
* **VS Code**

---

## How to Run the Programs
Ensure Python 3 is installed. Open a terminal or command prompt, navigate to the project folder, and run the desired task:

```bash
# To run the Pizza Calculator
python task1.py

# To run the Password Check
python task2.py