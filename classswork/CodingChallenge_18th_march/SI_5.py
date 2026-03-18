# Method 5: Check realistic values

def calculate_si(p, r, t):
    if p > 0 and r > 0 and t > 0:
        return (p * r * t) / 100
    else:
        return "Invalid values"

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print(calculate_si(p, r, t))