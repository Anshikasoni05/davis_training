# Method 3: Nested conditions

def calculate_si(p, r, t):
    if p >= 0:
        if r >= 0:
            if t >= 0:
                return (p * r * t) / 100
            else:
                return "Invalid time"
        else:
            return "Invalid rate"
    else:
        return "Invalid principal"

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print(calculate_si(p, r, t))