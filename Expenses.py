... from collections import defaultdict
... from datetime import datetime
... 
... class ExpenseTracker:
...     def __init__(self):
...         self.expenses = defaultdict(list)
... 
...     def add_expense(self, category, amount, description):
...         today = datetime.today().strftime('%Y-%m-%d')
...         self.expenses[today].append({"category": category, "amount": amount, "description": description})
... 
...     def get_monthly_summary(self, month, year):
...         monthly_expenses = defaultdict(float)
...         for date, expenses in self.expenses.items():
...             expense_month, expense_year, _ = date.split("-")
...             if expense_month == str(month) and expense_year == str(year):
...                 for expense in expenses:
...                     monthly_expenses[expense["category"]] += expense["amount"]
...         return monthly_expenses
... 
...     def save_expenses(self, filename):
...         with open(filename, "w") as file:
...             json.dump(self.expenses, file)
... 
...     def load_expenses(self, filename):
...         with open(filename, "r") as file:
...             self.expenses = json.load(file)
... 
... 
... def main():
...     tracker = ExpenseTracker()
...     filename = "expenses.json"
... 
...     try:
...         tracker.load_expenses(filename)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No previous expenses found.")

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter the expense category: ")
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            tracker.add_expense(category, amount, description)
            print("Expense added successfully!")

        elif choice == "2":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            monthly_summary = tracker.get_monthly_summary(month, year)
            if monthly_summary:
                print("Monthly Summary:")
                for category, total_amount in monthly_summary.items():
                    print(f"{category}: ${total_amount:.2f}")
            else:
                print("No expenses found for the specified month and year.")

        elif choice == "3":
            tracker.save_expenses(filename)
            print("Expenses saved successfully. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

