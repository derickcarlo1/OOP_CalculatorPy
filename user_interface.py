# Import the Calculator class from functions_cal.py file
from functions_cal import Calculator

# Import pyfiglet for ASCII art text
import pyfiglet

# ANSI color codes for colored text
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Create a UserInterface class
class UserInterface:
    def __init__(self):
        # Initialize an instance of the Calculator class
        self.calculator = Calculator()

    def display_result(self, result):
        # Display ASCII art for "Result"
        print(pyfiglet.figlet_format("Result"))
        # Display the result with yellow color
        print(f"{YELLOW}{result:.2f}{RESET}")

    def display_error(self, message):
        # Display ASCII art for "Error"
        print(pyfiglet.figlet_format("Error"))
        # Display the error message with red color
        print(f"{RED}{message}{RESET}")

    def get_number_input(self, prompt):
        while True:
            try:
                # Get user input as a float number
                number = float(input(prompt))
                # Return the valid number
                return number
            except ValueError:
                # Handle the case when the user enters an invalid number
                self.display_error("Please enter a valid number")

    def get_operation_input(self):
        while True:
            # Ask the user to choose an operation
            operation = input(f"{GREEN}Choose an operation (+, -, *, /): {RESET}")
            if operation in ["+", "-", "*", "/"]:
                # Return the valid operation
                return operation
            else:
                # Handle the case when the user enters an invalid operation
                self.display_error("Invalid operation. Please choose from +, -, *, /")


# Create an instance of the UserInterface class

# Run the calculator using the user interface
