# Method 3: Slab-based billing

def calculate_bill(units):
    if units <= 100:
        return units * 5
    else:
        return units * 7

units = int(input("Enter units: "))
print("Total bill:", calculate_bill(units))