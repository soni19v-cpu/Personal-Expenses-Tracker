import csv
from datetime import datetime

# File to store expenses
EXPENSE_FILE = 'expenses.csv'

def initialize_file():
    """Initializes the CSV file with headers if it doesn't exist."""
    try:
        with open(EXPENSE_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass # File already exists

def add_transaction(transaction_type, category, amount, description):
    """Adds a new transaction to the expense file."""
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, transaction_type, category, amount, description])
    print(f"{transaction_type} added successfully!")

def view_transactions():
    """Displays all recorded transactions."""
    initialize_file() # Ensure file exists before reading
    with open(EXPENSE_FILE, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) # Skip header row
        print(f"{header[0]:<20} {header[1]:<10} {header[2]:<15} {header[3]:<10} {header[4]:<30}")
        print("-" * 85)
        for row in reader:
            print(f"{row[0]:<20} {row[1]:<10} {row[2]:<15} {float(row[3]):<10.2f} {row[4]:<30}")

def get_summary():
    """Calculates and displays a summary of expenses and income."""
    initialize_file()
    total_income = 0
    total_expenses = 0
    category_expenses = {}

    with open(EXPENSE_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        for row in reader:
            transaction_type = row[1]
            amount = float(row[3])
            category = row[2]

            if transaction_type.lower() == 'income':
                total_income += amount
            elif transaction_type.lower() == 'expense':
                total_expenses += amount
                category_expenses[category] = category_expenses.get(category, 0) + amount

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${total_income - total_expenses:.2f}")
    print("\nExpenses by Category:")
    for category, amount in category_expenses.items():
        print(f"  {category}: ${amount:.2f}")

def main():
    initialize_file() # Ensure the file is ready at startup
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category (e.g., Salary, Gift): ")
            description = input("Enter description: ")
            add_transaction('Income', category, amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (e.g., Food, Transport): ")
            description = input("Enter description: ")
            add_transaction('Expense', category, amount, description)
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            get_summary()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
