# Method 4: Start from first even number

def print_even(n):
    if n >= 2:
        for i in range(2, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
    else:
        print("No even numbers")

n = int(input("Enter N: "))
print_even(n)