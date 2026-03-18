# Method 9: Using if-elif ladder

def calculate_si(p, r, t):
    if p < 0:
        return "Invalid principal"
    elif r < 0:
        return "Invalid rate"
    elif t < 0:
        return "Invalid time"
    else:
        return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print(calculate_si(p, r, t))