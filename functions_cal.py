import operator

# Create class
class Calculator:
    # Method add/plus
    def add(self, num1, num2):
        return operator.add(num1, num2)
    # Method substract/minus
    def subtract(self, num1, num2):
        return operator.sub(num1, num2)
    # Method multiplication/times
    def multiply(self, num1, num2):
        return operator.mul(num1, num2)
    # Method division/divide
    def divide(self, num1, num2):
        return operator.truediv(num1, num2)

