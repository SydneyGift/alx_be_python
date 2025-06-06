#Define arithmetic operations 
def perform_operation(num1, num2, operations):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
#Define the operation parameters
    def operations(operation_to_be_performed):
        operation_to_be_performed = str(input("Which operation would you like to perform? (add, subtract, multiply, divide)")).strip().lower
        match operation_to_be_performed:
            case 'add':
                result = num1 + num2
            case 'subtract':
                result = num1 - num2
            case 'multiply':
                result = num1 * num2
            case 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide a number by zero")