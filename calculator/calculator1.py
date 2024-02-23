class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Cannot divide by zero")
        return x / y

    def perform_calculation(self, expression):
        parts = expression.split()
        if len(parts) != 3:
            return "Error: Invalid input format. Please enter in the format 'number operator number'"
        
        num1, operation, num2 = parts
        operation_func = self.operations.get(operation)
        if not operation_func:
            return "Error: Invalid operation"
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            return "Error: Invalid input"
        
        try:
            result = operation_func(num1, num2)
        except Exception as e:
            return f"Error: {str(e)}"
        
        return result


calc = Calculator()
expression = input("Enter the expression (in the format 'number operator number'): ")

result = calc.perform_calculation(expression)
print("Result:", result)
