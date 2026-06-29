#!/usr/bin/env python3
# Give the user 3 attempts to guess the secret code (42), with feedback after each guess

#Giving the secret code number, and the number of attempts possible
secret_code = 42
max_attempts = 3
attempts = 0

#Writing the script with a while statement to make sure the number of attempts does not cross the max attempts threshold
while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the secret code: "))
    attempts += 1
#Defining what happens if the guess is correct or wrong
    if guess == secret_code:
        print("Correct! You cracked the code.")
        break
    elif guess < secret_code:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Out of attempts. The secret code was {secret_code}.")
