
employees = []

# Function to add an employee
def add_employee(name, age, salary):
    employee = {
        'name': name,
        'age': age,
        'salary': salary
    }
    employees.append(employee)

# Function to display all employee details
def display_employees():
    if not employees:
        print("No employees found.")
        return
    for index, employee in enumerate(employees, start=1):
        print(f"Employee {index}:")
        print(f"Name: {employee['name']}")
        print(f"Age: {employee['age']}")
        print(f"Salary: {employee['salary']}\n")

# Function to find an employee by name
def find_employee(name):
    for employee in employees:
        if employee['name'].lower() == name.lower():
            print(f"Employee found: Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}")
            return
    print(f"Employee named {name} not found.")
