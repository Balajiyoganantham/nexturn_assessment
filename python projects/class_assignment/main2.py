from employee import add_employee, display_employees, find_employee

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Find Employee by Name")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = float(input("Enter employee salary: "))
            add_employee(name, age, salary)
            print(f"Employee {name} added successfully.")
        elif choice == '2':
            display_employees()
        elif choice == '3':
            name = input("Enter the name of the employee to find: ")
            find_employee(name)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")
main()