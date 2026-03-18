#Program to calculate final bill after discount
# Method 6: Validate both price and discount

def calculate_bill(price, discount):
    if price > 0:
        if 0 <= discount <= 100:
            return price - (price * discount / 100)
        else:
            return "Invalid discount"
    else:
        return "Invalid price"

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print("Result:", calculate_bill(price, discount))