import csv
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print(" Expense added successfully!\n")

def view_expenses():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))
    print()

def total_expenses():
    total = 0
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f" Total Expenses: {total}\n")

def menu():
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

def main():
    initialize_file()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice\n")

if __name__ == "__main__":
    main()
