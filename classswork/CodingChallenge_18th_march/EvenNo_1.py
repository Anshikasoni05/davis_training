# Method 1: Print even numbers using function

def print_even(n):
    # Loop from 1 to n
    for i in range(1, n + 1):
        # Check even condition
        if i % 2 == 0:
            print(i, end=" ")

# Input
n = int(input("Enter N: "))

# Function call
print_even(n)