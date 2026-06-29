age = int(input("Enter your age: "))
gold = int(input("How many gold coins do you have? "))

if age >= 18 and gold >= 20:
    print("Welcome to the club!")
else:
    print("Entry denied. You need to be 18+ and carry at least 20 gold coins.")
