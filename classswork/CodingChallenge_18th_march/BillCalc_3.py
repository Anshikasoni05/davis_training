# Method 3: Check valid discount using function with if condition
#Program to calculate final bill after discount
def calculate_bill(price, discount):
    # Check if discount is valid
    if discount >= 0 and discount <= 100:
        return price - (price * discount / 100)
    else:
        return "Invalid discount"

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print("Result:", calculate_bill(price, discount))