# Method 4: Different discount slabs
# program to calculate final bill after discount using function with multiple conditions

def calculate_bill(price, discount):
    if discount < 10:
        return price - (price * discount / 100)
    elif discount <= 50:
        return price - (price * discount / 100)
    else:
        return "Too much discount not allowed"

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print("Final price:", calculate_bill(price, discount))