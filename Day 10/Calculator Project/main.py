from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


# Define the operations dictionary
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    continue_calculation = True
    first_number = float(input("Type the first number: "))

    while continue_calculation:
        operator = input("Type a mathematical operator (+, -, *, /): ")
        if operator not in operations:
            print("Invalid operator. Please choose from +, -, *, /.")
            continue

        second_number = float(input("Type the second number: "))

        # Perform the calculation
        calculation_function = operations[operator]
        result = calculation_function(first_number, second_number)

        print(f"The result of {first_number} {operator} {second_number} is: {result}")

        # Ask if the user wants to continue with the previous result
        user_choice = input(
            f"Do you want to continue with the result {result}? Type 'y' for yes or 'n' for no: ").lower()
        if user_choice == 'y':
            first_number = result
        else:
            continue_calculation = False
            # Reset for a new calculation
            calculator()


# Start the calculator program
calculator()


