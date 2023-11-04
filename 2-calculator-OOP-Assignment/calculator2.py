class Calculator:
    def __init__(self):
        self.operators = {'A': 'Addition', 'B': 'Subtraction', 'C': 'Multiplication', 'D': 'Division'}

    def display_menu(self):
        print("Choose an operation:")
        for key, value in self.operators.items():
            print(f"{key}: {value}")

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return abs(num1 - num2)

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."

    def perform_calculation(self, operator, num1, num2):
        if operator.upper() == 'A':
            return self.add(num1, num2)
        elif operator.upper() == 'B':
            return self.subtract(num1, num2)
        elif operator.upper() == 'C':
            return self.multiply(num1, num2)
        elif operator.upper() == 'D':
            return self.divide(num1, num2)
        else:
            return "Invalid operation."

if __name__ == "__main__":
    name = input('Please enter your name: ')
    print("Hello", name.upper())

    calculator = Calculator()
    calculator.display_menu()

    try:
        operator = input("Enter your choice of operation (A, B, C, or D): ")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        result = calculator.perform_calculation(operator, num1, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numeric inputs.")
    except Exception as error:
        print(f"Oops, an Error occurred: {str(error)}")
