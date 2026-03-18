# Method 2: Validate inputs

def calculate_si(p, r, t):
    if p < 0 or r < 0 or t < 0:
        return "Invalid input"
    else:
        return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", calculate_si(p, r, t))