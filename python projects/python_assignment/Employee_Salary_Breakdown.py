basic_salary = float(input("Enter your basic salary: "))
tax_rate = float(input("Enter your tax rate (as a percentage): ")) / 100
bonus = float(input("Enter your bonus: "))

tax_deductions = basic_salary * tax_rate
net_salary = basic_salary + bonus - tax_deductions

print(f"Total Deductions: ${tax_deductions:.2f}")
print(f"Net Salary: ${net_salary:.2f}")
