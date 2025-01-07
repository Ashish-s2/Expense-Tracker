import json

# File to store expense data
DATA_FILE = 'expenses.json'

# Function to load expenses from file
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist
    except json.JSONDecodeError:
        return []  # Return an empty list if file is empty or corrupt

# Function to save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add an expense
def add_expense(title, amount, category, date):
    expenses = load_expenses()

    # Create a new expense entry
    new_expense = {
        'title': title,
        'amount': float(amount),
        'category': category,
        'date': date
    }

    # Add to the list and save
    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("\nExpenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['title']} - ${expense['amount']} - {expense['category']} - {expense['date']}")

# Main Menu
def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter Title: ")
            amount = input("Enter Amount: ")
            category = input("Enter Category: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            add_expense(title, amount, category, date)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
