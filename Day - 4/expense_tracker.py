import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    """Add a new expense to the CSV file."""
    try:
        date = input("Enter Date (YYYY-MM-DD): ")

        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")

        category = input("Enter Category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        note = input("Enter Note (optional): ").strip()

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expense added successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid date and amount.")


def view_expenses():
    """Display all expenses and calculate the total amount."""
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            total = 0
            found = False

            print("\nExpense Records")
            print("-" * 70)

            for expense in reader:
                found = True

                print(f"Date     : {expense['Date']}")
                print(f"Category : {expense['Category']}")
                print(f"Amount   : {float(expense['Amount']):.2f}")
                print(f"Note     : {expense['Note']}")
                print("-" * 70)

                total += float(expense["Amount"])

            if not found:
                print("No expenses recorded.")
            else:
                print(f"Total Amount Spent: {total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


def category_summary():
    """Display total spending for each category."""
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            summary = {}

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

            if not summary:
                print("No expenses recorded.")
                return

            print("\nCategory-wise Spending Summary")
            print("-" * 40)

            for category, total in summary.items():
                print(f"{category}: {total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


def main():
    """Display the menu and handle user choices."""
    initialize_file()

    while True:
        print("\n===== Expense Tracking System =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using the Expense Tracking System.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()