class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def list_expenses(self):
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense['description']}: ${expense['amount']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            tracker.list_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()