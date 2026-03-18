#Program to calculate final bill after discount

# Taking input from user
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

# Calculating discount amount
discount_amount = price * discount / 100

# Final price after discount
final_price = price - discount_amount

# Display result
print("Final price after discount:", final_price)