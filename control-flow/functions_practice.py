#Function to return True if the string "cat" and "dog" appear the same number of times in the given string
def cat_dog(string):#Define the function call
  count_cat = string.count('cat')#Count the occurrences of the word 'cat' in the string
  count_dog = string.count('dog')#Count the occurrence of the word 'dog' in the string
  if count_cat == count_dog:#compare the two and greturn a value
    answer = True
  else:
    answer = False
  return answer

#Function to greet user by name
def greetings(username):#Defines the function call
  username = str(input("Enter your name: "))#Store users name in a variable called name
print(f"Hello," "{username}")#To greet the user print out Hello name on the screen.