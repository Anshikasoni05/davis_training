# Method 3: Explicit if-else

def print_even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")
        else:
            continue   # skip odd numbers

n = int(input("Enter N: "))
print_even(n)