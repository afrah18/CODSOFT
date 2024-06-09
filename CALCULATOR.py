
print("Simple Calculator")
print("Operations: +, -, *, /")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is undefined."
else:
    result = "Invalid operation!"
print(f"The result is: {result}")


# Simple Calculator
# Operations: +, -, *, /
# Enter the first number: 1
# Enter the second number: 1
# Enter the operation (+, -, *, /): +
# The result is: 2.0

# Simple Calculator
# Operations: +, -, *, /
# Enter the first number: 1
# Enter the second number: 1
# Enter the operation (+, -, *, /): -
# The result is: 0.0

# Simple Calculator
# Operations: +, -, *, /
# Enter the first number: 1
# Enter the second number: 1
# Enter the operation (+, -, *, /): *
# The result is: 1.0

# Simple Calculator
# Operations: +, -, *, /
# Enter the first number: 1
# Enter the second number: 1
# Enter the operation (+, -, *, /): /
# The result is: 1.0
