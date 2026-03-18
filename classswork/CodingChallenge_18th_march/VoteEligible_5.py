# Method 5: Age categories using function with multiple conditions
#Program to check whether a person is eligible to vote using multiple conditions


def check_vote(age):
    if age < 0:
        return "Invalid"
    elif age < 18:
        return "Not Eligible"
    elif age <= 100:
        return "Eligible"
    else:
        return "Invalid age range"

age = int(input("Enter age: "))
print(check_vote(age))