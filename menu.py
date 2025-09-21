# Menu module for Burger Billing System

# Menu items with prices
menu = {
    1: {"name": "Aloo Tikki", "price": 5},
    2: {"name": "Maharaja", "price": 10},
    3: {"name": "Mac Special", "price": 15}
}

# Function to display menu
def display_menu():
    print("\n" + "*" * 40)
    print("\tBURGER MENU")
    print("*" * 40)
    print("Sr.\tName\t\tPrice")
    print("-" * 40)
    
    for sr, item in menu.items():
        # Adjust spacing based on name length
        tab = "\t" if len(item["name"]) >= 8 else "\t\t"
        print(f"{sr}.\t{item['name']}{tab}${item['price']}")
    
    print("-" * 40)