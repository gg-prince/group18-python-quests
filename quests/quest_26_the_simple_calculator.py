#!/usr/bin/env python3
# Simple calculator: asks for two numbers and an operation, then computes the result


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()

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

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
