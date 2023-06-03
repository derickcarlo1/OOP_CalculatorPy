# Import the Calculator class from functions_cal.py file
from functions_cal import Calculator
from calupdatebyderick import updatedcalbyderick

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
        self.calculator = updatedcalbyderick()

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
            operation = input(f"{GREEN}Choose an operation (+, -, *, /, ^){RESET} {BLUE}Kindly reminder- if you chose cube operation (^), the number that will be cubed is only the first number you entered, regardless what you input in 2nd number: {RESET}")
            if operation in ["+", "-", "*", "/", "^"]:
                # Return the valid operation
                return operation
            else:
                # Handle the case when the user enters an invalid operation
                self.display_error("Invalid operation. Please choose from +, -, *, /, ^")

    def run_calculator(self):
        while True:
            try:
                # Get the first number from the user
                num1 = self.get_number_input(f"{GREEN}Enter the first number: {RESET}")
                # Get the second number from the user
                num2 = self.get_number_input(f"{GREEN}Enter the second number: {RESET}")
                # Get the operation from the user
                operation = self.get_operation_input()

                # Perform the calculation based on the chosen operation
                if operation == "+":
                    result = self.calculator.add(num1, num2)
                elif operation == "-":
                    result = self.calculator.subtract(num1, num2)
                elif operation == "*":
                    result = self.calculator.multiply(num1, num2)
                elif operation == "/":
                    result = self.calculator.divide(num1, num2)
                elif operation == "^":
                    result = self.calculator.cube(num1)


                # Display the result of the calculation
                self.display_result(result)
            except ZeroDivisionError:
                # Handle the case when the user tries to divide by zero
                self.display_error("Cannot divide by zero")

            # Ask the user if they want to try again
            choice = input(f"{GREEN}Do you want to try again? (y/n): {RESET}")
            if choice.lower() == "n":
                # Display ASCII art for "Thank you!" and exit the loop
                print(pyfiglet.figlet_format("Thank you!"))
                break
            elif choice.lower() != "y":
                # Handle the case when the user enters an invalid choice
                self.display_error("Invalid input. Please enter either 'y' or 'n'")

# Create an instance of the UserInterface class
ui = UserInterface()
# Run the calculator using the user interface
ui.run_calculator()