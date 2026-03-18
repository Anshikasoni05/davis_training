# Method 2: Validate units

def calculate_bill(units):
    if units < 0:
        return "Invalid units"
    else:
        return units * 5

units = int(input("Enter units: "))
print("Total bill:", calculate_bill(units))