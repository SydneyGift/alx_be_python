#Ask user for their monthly income and assign it a variable income

income = int(input("Enter your monthly income:"))

#Ask user for their total expenses per month and assign it a variable

total_expenses = int(input("Enter your total monthly expenses:"))

#Calculate monthly savings by subtracting expenses from income

monthly_savings = income - total_expenses

#Project annual savings with a simple interest of 5%

annual_savings = monthly_savings * 12 + (monthly_savings *12 * 0.05)

#Output the users monthly savings and projected annual savings with interest

print ("Your monthly savings are:", monthly_savings)
print ("Projected savings after one year, with interest, is:", annual_savings)
