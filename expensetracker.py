# MY EXPENSE TRACKER PROJECT

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = float(amount)
        self.category = category

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_to_list(self):
        choice1a = input("Enter expense name: ")
        
        while True:
            choice1b = input("Enter expense amount: ")
            try:
                choice1b = float(choice1b)
                if choice1b < 0:
                    print("number can't be less than zero")
                    continue
                break
            except ValueError:
                print("Please enter a valid amount")
           
        choice1c = input("Enter expense category: ")
        num1 = Expense(choice1a, choice1b, choice1c)
        self.expenses.append(num1)
        print("Expense successfully added")
        
    def view_expenses(self):
        print("_______Your Expenses_______")
        for expense in self.expenses:
           print(f"Name: {expense.name}, Amt: {expense.amount}, Category: {expense.category}")

    def categorize(self):
       new_group = {}
       for expense in self.expenses:
              if expense.category not in new_group:
                new_group[expense.category] = []
              new_group[expense.category].append(expense.name)
        
       for category, names in new_group.items():
            print(f"{category}: {', '.join(names)}")

    def calc_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print("Total:", total)

    def filter_list(self):
        found = False
        choice = input("Enter the category you want to filter: ").lower()
        for expense in self.expenses:
            if choice == expense.category:
                print(expense.name)
                found = True
        if not found:
            print("Invalid input")
            
    def del_item(self):
        found = False
        num6 = input("Enter an expense to delete: ")
        for expense in self.expenses:
            if expense.name == num6:
                found = True
                self.expenses.remove(expense)
                print("item successfully removed")
                self.view_expenses()
                break
        if not found:
            print("Item not found in your Expenses")

def main():
    is_running = True

    spend = ExpenseManager()

    while is_running:
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Categorize expenses")
        print("4. Calculate total spending")
        print("5. Filter by category")
        print("6. Delete an expense")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            spend.add_to_list()
        elif choice == '2':
            spend.view_expenses()
        elif choice == '3':
            spend.categorize()
        elif choice == '4':
            spend.calc_total()
        elif choice == '5':
            spend.filter_list()
        elif choice == '6':
            spend.del_item()
        elif choice == '7':
                is_running = False
        else:
            print("invalid input!")

if __name__ == '__main__':
    main()
