#Implementing a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
def safe_divide(float(numerator), float(denominator)):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "The input is not a  numeric value"