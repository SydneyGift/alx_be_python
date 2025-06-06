#Program to display current date as well as calculate a future date
from datetime import datetime, timedelta

#Define a function to display current date and time
def display_current_datetime():
    current_date = datetime.now()#Collecting the full date and time
    #Display the current date and time
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

#Call the function to display the current date and time.
display_current_datetime()

#Define a functiion to calculate a future date based on user input.
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    #Convert the user input into a duration
    added_days = timedelta(days = number_of_days)
    #Calculate the future date
    future_date = datetime.now() + added_days#Using the date only
    print("Future  date: ", future_date.strftime('%Y-%m-%d'))

calculate_future_date()