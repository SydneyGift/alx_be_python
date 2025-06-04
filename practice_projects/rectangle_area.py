#Function to calculate area of a rectangle by taking two parameters

#Take input from user and store in vartiables
number1 = int(input("What is the length of the rectangle? "))
number2 = int(input("What is the width of the rectangle? "))

def rectangle_area(length, width):#Define the function to calculate the area
    area = length * width
    return area

print("The area is:",rectangle_area(number1, number2))#Call the function and print it on screen to see if it works