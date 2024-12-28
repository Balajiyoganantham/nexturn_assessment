age = int(input("Enter the customer's age: "))

if age < 5:
    price = 0
elif 5 <= age <= 12:
    price = 5
elif 13 <= age <= 60:
    price = 12
else:
    price = 8

print(f"Ticket Price: ${price}")
