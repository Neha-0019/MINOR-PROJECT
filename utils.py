# Utils module for Burger Billing System
import os

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get valid integer input
def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number greater than or equal to {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number less than or equal to {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

# Function to get yes/no input
def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")