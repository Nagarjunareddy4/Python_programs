# Simple Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It includes error handling for division by zero and provides a user-friendly interface.
def add(x, y): # This function adds two numbers
    return x + y 
def subtract(x, y): # This function subtracts two numbers
    return x - y
def multiply(x, y): # This function multiplies two numbers
    return x * y
def divide(x, y): # This function divides two numbers
    # Check if the second number is zero to avoid division by zero error
    if y == 0:
        raise ValueError("Cannot divide by zero.") # Raise an error if y is zero
    return x / y
# Main program loop
print("Welcome to the Simple Calculator!")
while True: # Infinite loop to keep the calculator running
    print("\nSelect operation:") # Display the menu
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid Input")