#Define arithmetic operations 
def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = str(input("Which operation would you like to perform? (add, subtract, multiply, divide)")).strip().lower
    
    #match the various operation parameters
    # match operation:
    #         case 'add':
    #             result = num1 + num2
    #         case 'subtract':
    #             result = num1 - num2
    #         case 'multiply':
    #             result = num1 * num2
    #         case 'divide':
    #             if num2 != 0:
    #                 result = num1 / num2
    #             else:
    #                 print("Cannot divide a number by zero")
    #         case_:
    #             print("Unnsupported operation selected")
    #Use if statemets in order to satisfy == conditions on checker
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Unsupported operation selected"