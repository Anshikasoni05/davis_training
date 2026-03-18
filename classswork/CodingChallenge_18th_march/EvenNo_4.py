# Method 5: Nested condition

def print_even(n):
    if n > 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
    else:
        print("Invalid input")

n = int(input("Enter N: "))
print_even(n)