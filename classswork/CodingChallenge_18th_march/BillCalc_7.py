# Method 7: Ask user if discount should be applied
#Program to calculate final bill after discount
def calculate_bill(price, discount, apply_discount):
    if apply_discount == "yes":
        return price - (price * discount / 100)
    else:
        return price

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))
choice = input("Apply discount? (yes/no): ")

print("Final price:", calculate_bill(price, discount, choice))