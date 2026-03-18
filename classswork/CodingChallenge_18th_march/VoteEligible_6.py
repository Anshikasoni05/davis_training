# Method 6: Check age + citizenship
#function with two inputs age and citizenship check 
def check_vote(age, citizen):
    if citizen == "yes":
        if age >= 18:
            return "Eligible"
        else:
            return "Not Eligible"
    else:
        return "Not Eligible (Not a citizen)"

age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")

print(check_vote(age, citizen))