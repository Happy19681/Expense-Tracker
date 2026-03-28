expenses = []

def add_expense():
    name = input("Enter your name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
    else:
        for exp in expenses:
            print(exp)
        print()


while True:
    print("=="*30)
    print(' '* 5 ,"Expense Tracker")
    print("=="*30)
    print(' '* 5 ,"1. Add Expense")
    print(' '* 5 ,"2. View Expenses")
    print(' '* 5 ,"3. Quit")

    choice = input("Choose a number (1-3): ")

    match choice:
        case "1":
            add_expense()
        case "2":
            view_expenses()
        case "3":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice, try again.\n")