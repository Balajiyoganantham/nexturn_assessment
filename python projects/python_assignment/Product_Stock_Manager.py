inventory = {}

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product.lower() == 'done':
        break
    quantity = int(input(f"Enter stock quantity for {product}: "))
    inventory[product] = quantity

print("\nInventory List:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")
