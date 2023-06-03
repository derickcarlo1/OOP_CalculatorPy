# Import the Calculator class from functions_cal.py file
from functions_cal import Calculator

# Create a new class called updatedcalbyderick (overriding)
class updatedcalbyderick(Calculator):
    # Override the multiply method from the Calculator class
    def multiply(self, num1, num2):
        return num1 ** num2  # Calculate exponentiation instead of multiplication
