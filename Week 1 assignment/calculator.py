# Basic Calculator Program

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to input a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero is not allowed!"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation!"

# Display the result
print(f"{num1} {operation} {num2} = {result}")