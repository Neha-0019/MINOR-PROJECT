# Order module for Burger Billing System
from menu import menu
from utils import get_int_input, get_yes_no_input

# Function to process a single order
def process_order():
    # Get burger selection
    burger_id = get_int_input("\nEnter the Sr. number of the burger you want to order: ", 1, len(menu))
    selected_burger = menu[burger_id]
    
    # Get quantity
    quantity = get_int_input("How many quantity? ", 1)
    
    # Check for student discount
    is_student = get_yes_no_input("Are you a student? (y/n): ")
    
    # Check for delivery
    delivery_needed = get_yes_no_input("Do you want delivery? (y/n): ")
    
    # Check for tip
    tip_amount = 0
    if get_yes_no_input("Do you want to give a tip? (y/n): "):
        print("\nHow much tip would you like to give?")
        print("1. $2")
        print("2. $5")
        print("3. $10")
        tip_choice = get_int_input("Enter your choice (1-3): ", 1, 3)
        tip_amount = [2, 5, 10][tip_choice - 1]
    
    # Calculate bill
    subtotal = selected_burger["price"] * quantity
    
    # Apply student discount if applicable
    discount = 0
    if is_student:
        discount = subtotal * 0.2  # 20% discount
    
    # Apply delivery charge if applicable
    delivery_charge = 0
    if delivery_needed:
        delivery_charge = subtotal * 0.05  # 5% delivery charge
    
    # Calculate final total
    total = subtotal - discount + delivery_charge + tip_amount
    
    # Return order details for the bill
    return {
        "burger": selected_burger,
        "quantity": quantity,
        "subtotal": subtotal,
        "discount": discount,
        "delivery_charge": delivery_charge,
        "tip": tip_amount,
        "total": total
    }

# Function to print the bill
def print_bill(orders):
    from utils import clear_screen
    clear_screen()
    print("\n" + "*" * 50)
    print("*" * 15 + " FINAL BILL " + "*" * 15)
    print("*" * 50)
    print("Sr.\tName\t\tPrice\tQuantity\tTotal")
    print("-" * 50)
    
    grand_total = 0
    total_discount = 0
    total_delivery = 0
    total_tip = 0
    
    for i, order in enumerate(orders, 1):
        burger = order["burger"]
        # Adjust spacing based on name length
        tab = "\t" if len(burger["name"]) >= 8 else "\t\t"
        print(f"{i}.\t{burger['name']}{tab}${burger['price']}\t{order['quantity']}\t\t${order['subtotal']}")
        
        grand_total += order["subtotal"]
        total_discount += order["discount"]
        total_delivery += order["delivery_charge"]
        total_tip += order["tip"]
    
    print("-" * 50)
    print(f"\t\t\t\t\t${grand_total:.1f}")
    
    if total_discount > 0:
        print(f"Student discount 20%\t\t\t-${total_discount:.1f}")
    
    if total_delivery > 0:
        print(f"Delivery charge 5%\t\t\t+${total_delivery:.1f}")
    
    if total_tip > 0:
        print(f"Tip\t\t\t\t\t${total_tip:.1f}")
    
    print("-" * 50)
    final_total = grand_total - total_discount + total_delivery + total_tip
    print(f"Total bill\t\t\t\t${final_total:.1f}")
    print("\nThank you and come again! >>>>>>>>>>>>>>>>>>>>>>>>>>")