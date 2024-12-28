salary = float(input("Enter your monthly salary: "))
rent = float(input("Enter your rent cost: "))
groceries = float(input("Enter your groceries cost: "))
utilities = float(input("Enter your utility costs: "))

total_expenses = rent + groceries + utilities
surplus = salary - total_expenses

print(f"Surplus: ${surplus:.2f}")
print(f"Rent: {(rent/salary)*100:.2f}%")
print(f"Groceries: {(groceries/salary)*100:.2f}%")
print(f"Utilities: {(utilities/salary)*100:.2f}%")
