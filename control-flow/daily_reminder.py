#A daily reminder and urgency program.
#take input from user for various situations.

task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

#Use match case to cater for various scenarios based on if they are time bound or not.

match time_bound:
    case "yes":
        while time_bound == "yes":
            if priority == "high":
                print(f"{task} is a high priority task that requires immediate attention today!")
            elif priority == "medium":
                print(f"{task} is a medium priority task that requires immediate attention today!")
            elif priority == "low":
                print(f"{task} is a low priority task that requires immediate attention today!")
            else:
                print("Incorrect input for priority")
            break
    case "no":
        while time_bound == "no":
            if priority == "high":
                print(f"{task} is a high priority task. Consider completing it when you have free time.")
            elif priority == "medium":
                print(f"{task} is a medium priority task. Consider completing it when you have free time.")
            elif priority == "low":
                print(f"{task} is a low priority task. Consider completing it when you have free time.")
            else:
                print("Incorrect input for priority")
            break
