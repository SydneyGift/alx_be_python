#Program to generate a random set of numbers between 1 and 10. The quantity of the numbers is defined by a user. Lastly, duplicates are removed.
import random
values = int(input("How many values of numbers betweeen 1 and 10 do you want in your set? "))

"""Generate a random list between 1 and 10"""
random_list1 = random.choices(range(1,11), k = values)
print("Here are the numbers", random_list1)
print("Removing duplicates...")

#Remove duplicates in the generated set
"""To remove the duplicates, I convert the list into a set"""
list_to_set = set(random_list1)
print(list_to_set)
