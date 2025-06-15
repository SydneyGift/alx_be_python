#Practice handling errors

#Divide by zero in a program that takes two numbers as input from the user and divides the first number by the second number.

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

try:
    division = num1 / num2
    print(f"{num1} divided by {num2} is {division}")

except ZeroDivisionError:
    print("You cannot divide by zero")