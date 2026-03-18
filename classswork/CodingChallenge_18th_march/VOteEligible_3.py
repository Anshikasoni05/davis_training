# Program to check whether a person is eligible to vote
# Method 3: Nested if

def check_vote(age):
    if age >= 0:
        if age >= 18:
            return "Eligible"
        else:
            return "Not Eligible"
    else:
        return "Invalid age"

age = int(input("Enter age: "))
print(check_vote(age))