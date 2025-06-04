import calculator
import time

def main(num1, num2):
    result = None
    if operator == '+':
        result = calculator.add(num1, num2)
    elif operator == '-':
        result = calculator.subtract(num1, num2)
    elif operator == '*':
        result = calculator.multiply(num1, num2)
    elif operator == '/':
        result = calculator.divide(num1, num2)
    return result
if __name__ == "__main__":
    num1 = 5
    num2 = 3
    print("Welcome to the calculator program!")
    print("===" *11)
    time.sleep(1)
    operator = input("Enter an operator (+, -, *, /): ")
    time.sleep(0.5)
    print(f"The result  = {main(num1, num2)}")