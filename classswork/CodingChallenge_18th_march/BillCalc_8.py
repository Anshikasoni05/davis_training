# Method 8: Apply discount only if price > 500
#Program to calculate final bill after discount
def calculate_bill(price, discount):
    if price > 500:
        return price - (price * discount / 100)
    else:
        return price  # no discount

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print("Final price:", calculate_bill(price, discount))