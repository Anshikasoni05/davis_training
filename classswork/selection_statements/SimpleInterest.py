# Program to calculate Simple Interest
# This program takes Principal, Rate, and Time as input
# It validates the data to ensure the user enters positive numbers

# Taking principal amount input
principal = float(input("Enter the principal amount: "))

# Validate principal amount
if principal <= 0:
    print("Principal amount must be greater than 0.")
else:
    
    # Taking rate of interest input
    rate = float(input("Enter the rate of interest (in %): "))
    
    # Validate rate
    if rate <= 0:
        print("Rate of interest must be greater than 0.")
    else:
        
        # Taking time input
        time = float(input("Enter the time (in years): "))
        
        # Validate time
        if time <= 0:
            print("Time must be greater than 0.")
        else:
            
            # Formula for Simple Interest
            simple_interest = (principal * rate * time) / 100
            
            # Display result
            print("Simple Interest =", simple_interest)