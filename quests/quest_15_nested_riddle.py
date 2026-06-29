direction = input("Do you go left or right? ").lower()

if direction == "left":
    action = input("Do you swim or wait? ").lower()
    if action == "swim":
        print("You brave the current and discover a chest of gold. Treasure found!")
    else:
        print("You wait too long. The tide rises and you're stuck. Game over.")
else:
    print("You head right and walk straight into a sleeping dragon. Better luck next time!")
