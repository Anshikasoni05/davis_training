# Function to calculate final price
def calculate_bill(price, discount):
    return price - (price * discount / 100)

# Calling function
result = calculate_bill(1000, 10)

# Printing result
print("Final price:", result)