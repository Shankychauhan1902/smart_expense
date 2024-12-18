import os
import json
from datetime import datetime

class SmartExpenseTracker:
    def __init__(self):
        self.data_file = "expenses.json"
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.data_file, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['date']} | {expense['category']} | ${expense['amount']} | {expense['description']}")

    def generate_report(self):
        report = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in report:
                report[category] += amount
            else:
                report[category] = amount

        print("\nExpense Report:")
        for category, total in report.items():
            print(f"{category}: ${total:.2f}")

    def start(self):
        while True:
            print("\nSmart Expense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Generate Report")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount: "))
                    category = input("Enter category: ")
                    description = input("Enter description: ")
                    self.add_expense(amount, category, description)
                except ValueError:
                    print("Invalid input. Please enter a valid number for amount.")
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.generate_report()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = SmartExpenseTracker()
    tracker.start()
