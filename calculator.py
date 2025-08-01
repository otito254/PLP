# Simple Calculator Program

# Ask for the first number
num1 = float(input("Enter first number: "))

# Ask for the second number
num2 = float(input("Enter second number: "))

# Ask for the operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (1-4): ")

# Calculate based on the operation
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid choice! Please select 1-4.")