#A daily reminder and urgency program.
#take input from user for various situations.

task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

#Use match case to cater for various scenarios based on if they are time bound or not.

match priority:
    case "high":
        while priority == "high":
            if time_bound == "yes":
                print(f"{task} is a high priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"{task} is a high priority task. Consider completing it when you have free time.")
            else:
                print("Incorrect input for time bound")
            break
    case "medium":
        while priority == "high":
            if time_bound == "yes":
                print(f"{task} is a medium priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"{task} is a medium priority task. Consider completing it when you have free time.")
            else:
                print("Incorrect input for time bound")
            break
    case "low":
        while priority == "high":
            if time_bound == "yes":
                print(f"{task} is a low priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"{task} is a low priority task. Consider completing it when you have free time.")
            else:
                print("Incorrect input for time bound")
            break