# Method 4: Return True/False
# Program to check whether a person is eligible to vote
def is_eligible(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Enter age: "))

# Using result
if is_eligible(age):
    print("Eligible")
else:
    print("Not Eligible")