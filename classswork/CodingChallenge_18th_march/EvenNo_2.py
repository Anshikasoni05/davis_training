# Method 2: Validate input

def print_even(n):
    if n <= 0:
        print("Invalid input")
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")

n = int(input("Enter N: "))
print_even(n)