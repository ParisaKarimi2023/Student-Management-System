import csv
import os

FILE_NAME = "students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Major"])

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    major = input("Enter major: ")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name, age, major])

    print("Student added successfully!\n")

def view_students():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print("\t".join(row))
    print()

def search_student():
    search_id = input("Enter student ID to search: ")
    found = False

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["ID"] == search_id:
                print(row)
                found = True
                break

    if not found:
        print("Student not found\n")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    students = []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["ID"] != student_id:
                students.append(row)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Age", "Major"])
        writer.writeheader()
        writer.writerows(students)

    print("🗑️ Student deleted (if existed)\n")

def menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    initialize_file()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
