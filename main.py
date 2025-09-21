# filepath: burger_billing_system/main.py
import os
from menu import display_menu
from order import process_order, print_bill
from utils import get_yes_no_input, clear_screen

# Main function
def main():
    clear_screen()
    print("Welcome to Burger Billing System!")
    
    orders = []
    ordering = True
    
    while ordering:
        display_menu()
        orders.append(process_order())
        
        if len(orders) > 0:
            ordering = get_yes_no_input("\nDo you want to order anything else? (y/n): ")
    
    print_bill(orders)

# Run the program
if __name__ == "__main__":
    main()