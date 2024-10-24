child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
#expensive
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

print(f"Subtotal: ${subtotal}")