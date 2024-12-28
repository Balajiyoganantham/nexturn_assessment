while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    print("Invalid input. Please enter a valid name.")

while True:
    try:
        salary = float(input("Enter your salary: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid float for salary.")

while True:
    try:
        dependents = int(input("Enter the number of dependents: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of dependents.")
