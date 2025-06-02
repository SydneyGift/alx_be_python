# Program to return True if the string "cat" and "dog" appear the same number of times in the given string
string = input("Enter your input for cat_dog: ")
def cat_dog(string):
  if 'cat' == 'dog' in string:
    answer = "True"
  else:
    answer = "False"
    return answer