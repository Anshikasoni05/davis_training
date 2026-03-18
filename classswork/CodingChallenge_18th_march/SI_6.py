# Method 7: Warning for high rate

def calculate_si(p, r, t):
    if r > 20:
        print("Warning: High interest rate")
    return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", calculate_si(p, r, t))