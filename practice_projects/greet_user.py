#function to greet user and takes one parameter name

user = input("What is your name: ")
def greet(name):
    print(f"Hello {user}!")

greet(user)