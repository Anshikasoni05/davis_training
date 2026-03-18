# Method 7: Extra charge for high usage

def calculate_bill(units):
    if units > 200:
        return units * 5 + 100   # extra ₹100
    else:
        return units * 5

units = int(input("Enter units: "))
print("Total bill:", calculate_bill(units))