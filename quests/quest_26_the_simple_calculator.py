#!/usr/bin/env python3
# Simple calculator: asks for two numbers and an operation, then computes the result

#Defines the add function here
def add(a, b):
    return a + b

#Defines the subtract function here
def subtract(a, b):
    return a - b

#Defines the multiply function here
def multiply(a, b):
    return a * b

#Defines the divide function, and adds an if statement to ensure that the division is possible(division by zero is infinite)
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

#Defining the main function, and making it suitable for user input
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()
#Using if statements to control operations and outcomes, depending on what the user chose
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        result = "Error: unknown operation"
#Printing the final result of the user inputs
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
