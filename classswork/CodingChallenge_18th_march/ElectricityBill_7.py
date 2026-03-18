# Method 9: Different rate for peak hours

def calculate_bill(units, time):
    if time == "peak":
        return units * 7
    else:
        return units * 5

units = int(input("Enter units: "))
time = input("Enter time (peak/normal): ")

print("Total bill:", calculate_bill(units, time))