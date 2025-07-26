import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'

# Ensure the file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. Food, Transport, Bills): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added.\n")

def view_expenses(show_index=False):
    print("\n📋 All Expenses:")
    with open(FILENAME, 'r') as file:
        reader = list(csv.reader(file))
        for i, row in enumerate(reader):
            if show_index and i > 0:  # skip header
                print(f"[{i}] " + '\t'.join(row))
            else:
                print('\t'.join(row))
    print()
    return reader

def delete_expense():
    data = view_expenses(show_index=True)

    try:
        index = int(input("Enter the index of the expense to delete: "))
        if index == 0:
            print("❌ Cannot delete header row.")
            return
        if 0 < index < len(data):
            deleted = data.pop(index)
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"🗑️ Deleted: {deleted}")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Please enter a valid number.")

def total_spent():
    total = 0
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['Amount'])
    print(f"\n💰 Total Spent: ${total:.2f}\n")

def menu():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

#This checks if the current script is being run directly 
if __name__ == '__main__':
    menu()
