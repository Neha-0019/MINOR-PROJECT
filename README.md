# Burger Billing System

A simple Python application for managing burger orders and generating bills.

## Features

- Display a menu of burger options
- Take orders with quantity
- Apply student discounts (20%)
- Add delivery charges (5%)
- Include optional tips
- Generate detailed bills
- Support for multiple orders in a single session

## Project Structure

```
burger_billing_system/
├── __init__.py
├── src/
│   ├── __init__.py
│   ├── main.py       # Entry point of the application
│   ├── menu.py       # Menu display and data
│   ├── order.py      # Order processing and bill generation
│   └── utils.py      # Utility functions
└── README.md
```

## How to Run

1. Make sure you have Python installed
2. Navigate to the project directory
3. Run the application using:

```bash
python -m burger_billing_system.src.main
```

Or navigate to the src directory and run:

```bash
python main.py
```

## Usage

1. The program displays a burger menu
2. Select a burger by entering its number
3. Enter the quantity
4. Specify if you're a student (for discount)
5. Choose whether you want delivery
6. Decide if you want to give a tip
7. Optionally order more items
8. View your final bill