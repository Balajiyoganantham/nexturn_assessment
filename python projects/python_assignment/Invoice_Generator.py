name = input("Enter your name: ")
num_products = int(input("Enter the number of products you bought: "))

products = []
total_cost = 0

for i in range(num_products):
    product_name = input(f"Enter the name of product {i + 1}: ")
    product_price = float(input(f"Enter the price of {product_name}: "))
    products.append((product_name, product_price))
    total_cost += product_price

print(f"\nInvoice for {name}")
for product, price in products:
    print(f"{product}: ${price}")
print(f"Total Cost: ${total_cost}")
