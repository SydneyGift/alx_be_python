#An app that displays the multiplication table through ten of a number entered by a user

number = int(input("Enter a number to see its multiplication table:"))

for integer in range(1,11):
    multiplication = number * integer
    print(f"{number} * {integer} = {multiplication}")