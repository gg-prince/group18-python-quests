#!/usr/bin/env python3
# Print numbers 1 to 100, replacing multiples of 3 with "Fizz", 5 with "Buzz", and both with "FizzBuzz"

#Defining the range of figures that are allowed (1-100)

for i in range(1, 101):
#Using 'if' and 'and' statements to specify for numbers divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
#Using 'elif' statements to specify if the number is divisible by only 3 or 5
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
