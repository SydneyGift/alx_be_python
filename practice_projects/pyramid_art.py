#write a program that displays asterisks to resemble a pyramid
rows = 5
current_row = 1
while current_row <= rows:
    spaces = rows - current_row
    no_of_stars = current_row * 2 -1
    print(" " * spaces, "*" * no_of_stars)
    current_row += 1