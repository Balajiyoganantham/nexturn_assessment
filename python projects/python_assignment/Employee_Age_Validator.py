while True:
    try:
        age = int(input("Enter the employee's age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")
