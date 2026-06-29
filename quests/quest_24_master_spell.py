# This function asks the user for their age
# and returns it as an integer.
def ask_for_age():
    age = int(input("Enter your age: "))
    return age

# This function checks if the user can vote.
def can_they_vote(age):
    if age >= 18:
        print("You can vote.")
    else:
        print("You cannot vote yet.")

# Get the user's age.
user_age = ask_for_age()

# Pass the age to the voting function.
can_they_vote(user_age)
