# Program to calculate Simple Interest and validate input

# Taking input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Validation using if-else
if principal <= 0 or rate <= 0 or time <= 0:
    print("Invalid Input! Principal, Rate and Time must be positive values.")
else:
    # Simple Interest Formula
    simple_interest = (principal * rate * time) / 100
    
    print("Principal Amount:", principal)
    print("Rate of Interest:", rate)
    print("Time:", time)
    print("Simple Interest =", simple_interest)