# This function prints a personalized greeting.
# It uses the user's name and quest.
def personalized_greeting(name, quest):
    print(f"Hello {name}! Good luck with your {quest} quest.")

# Ask the user for their name.
name = input("Enter your name: ")

# Ask the user for their quest.
quest = input("Enter your quest: ")

# Call the function using the user's answers.
personalized_greeting(name, quest)
