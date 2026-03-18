# Method 6: Complete condition handling

def calculate_bill(units):
    if units < 0:
        return "Invalid units"
    elif units <= 100:
        return units * 5
    elif units <= 200:
        return units * 6
    else:
        return units * 8

units = int(input("Enter units: "))
print("Total bill:", calculate_bill(units))