import operator
import pyfiglet

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# define a function for performing the calculations
def calculate():
    try:
        # ask the user for two numbers and an operation
        num1 = float(input(f"{GREEN}Enter the first number: {RESET}"))
        num2 = float(input(f"{GREEN}Enter the second number: {RESET}"))
        operation = input(f"{GREEN}Choose an operation (+, -, *, /): {RESET}")
        
        # perform the calculation based on the chosen operation
        if operation == "+":
            result = operator.add(num1, num2)
        elif operation == "-":
            result = operator.sub(num1, num2)
        elif operation == "*":
            result = operator.mul(num1, num2)
        elif operation == "/":
            result = operator.truediv(num1, num2)

        # print the result of the calculation
        print(pyfiglet.figlet_format("Result"))
        print(f"{YELLOW}{result:.2f}{RESET}")
    except ValueError:
        # handle errors when the user enters invalid input
        print(pyfiglet.figlet_format("Error"))
        print(f"{RED}Please enter valid numbers{RESET}")
    except ZeroDivisionError:
        # handle errors when the user tries to divide by zero
        print(pyfiglet.figlet_format("Error"))
        print(f"{RED}Cannot divide by zero{RESET}")

# repeatedly ask the user to perform calculations
while True:
    calculate() # call the calculate function
    choice = input(f"{GREEN}Do you want to try again? (y/n): {RESET}")
    if choice.lower() == "n":
        print(pyfiglet.figlet_format("Thank you!"))
        break
    elif choice.lower() != "y":  # added an error if the user inputs something other than y or n
        print(pyfiglet.figlet_format("Error"))
        print(f"{RED}Invalid input. Please enter either 'y' or 'n'{RESET}")