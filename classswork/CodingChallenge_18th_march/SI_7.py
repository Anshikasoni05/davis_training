# Method 8: Check time duration

def calculate_si(p, r, t):
    if t > 10:
        return (p * r * t) / 100
    else:
        return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", calculate_si(p, r, t))