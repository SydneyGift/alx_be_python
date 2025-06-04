#Program to check if a number is even or odd

check = int(input("Enter the number you want to check if it is even or odd: "))

def even_or_odd(number):
    if number % 2 == 0:
        print(f"The number '{number}' is even.")
    else:
        print(f"The number '{number}' is odd.")

even_or_odd(check)