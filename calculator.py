"""
Simple Command-Line Calculator

Features:
- Supports +, -, *, /
- Validates every input the moment it is entered
- Handles divide-by-zero
- Calculation logic kept in separate functions (testable)
- Menu for repeated calculations, clearing the screen, or exiting
"""

import math
import os

OPERATORS = ("+", "-", "*", "/")


# ---------------------------------------------------------------
# Calculation logic (no input/print here, so it can be tested)
# ---------------------------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate(a, operator, b):
    """Apply the operator to a and b and return the result."""
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operator: {operator}")


# ---------------------------------------------------------------
# User input (each input is checked immediately)
# ---------------------------------------------------------------

def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        text = input(prompt).strip()
        try:
            number = float(text)
        except ValueError:
            print("  That's not a valid number. Please try again.")
            continue
        if not math.isfinite(number):
            print("  Please enter a regular number (not inf or nan).")
            continue
        return number


def get_operator():
    """Keep asking until the user enters a valid operator."""
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        if operator in OPERATORS:
            return operator
        print("  Invalid operator. Please choose one of: + - * /")


# ---------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------

def format_number(n):
    """Show 5.0 as 5, and tidy tiny float errors (0.1 + 0.2 -> 0.3)."""
    if n.is_integer():
        return str(int(n))
    return str(round(n, 10))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print()
    print("====== SIMPLE CALCULATOR ======")
    print("1. Calculate")
    print("2. Clear screen")
    print("3. Exit")


# ---------------------------------------------------------------
# Program flow
# ---------------------------------------------------------------

def run_calculation():
    a = get_number("Enter the first number: ")
    operator = get_operator()
    b = get_number("Enter the second number: ")

    try:
        result = calculate(a, operator, b)
    except ZeroDivisionError:
        print("  Error: you can't divide by zero.")
        return

    if not math.isfinite(result):
        print("  Error: the result is too large to display.")
        return

    print(f"  Result: {format_number(a)} {operator} {format_number(b)} = {format_number(result)}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            run_calculation()
        elif choice == "2":
            clear_screen()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
