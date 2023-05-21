from functions_cal import Calculator
from user_interface import UserInterface

# Create an instance of the UserInterface class
user_interface = UserInterface()
# Create an instance of the Calculator class
calculator = Calculator()

while True:
    # Get the operation name from the user
    operation_name = user_interface.get_operation_input()

    # Get the first and second numbers from the user
    first_number = user_interface.get_number_input("Enter the first number: ")
    second_number = user_interface.get_number_input("Enter the second number: ")

    try:
        # Perform the calculation based on the chosen operation
        result = calculator.perform_calculation(operation_name, first_number, second_number)
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero!")

    # Ask the user if they want to try again
    response = user_interface.retry()
    if response:
        continue
    else:
        break
