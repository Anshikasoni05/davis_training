# Method 4: Nested conditions

def calculate_bill(units):
    if units >= 0:
        if units <= 100:
            return units * 5
        else:
            return units * 7
    else:
        return "Invalid units"

units = int(input("Enter units: "))
print(calculate_bill(units))