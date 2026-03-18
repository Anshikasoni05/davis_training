# Method 4: If discount is 0
#Program to calculate final bill after discount

def calculate_bill(price, discount):
    if discount == 0:
        return price   # no change
    else:
        return price - (price * discount / 100)

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print("Final price:", calculate_bill(price, discount))