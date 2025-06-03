
#Start writing a guessing game for numbers between 1 and 10
import random

#Take a guess from the user and create loop for multiple guesses

def play_game():
    #Generate a random secret number
        secret_number = random.randint(1,10)
        while True:
            guess = int(input("I am thinking of a number between 1 and 10, can you guess it? "))

            match guess:
                case less if guess < secret_number:
                     print ("The number is less than what I am thinking of, take another guess. ")
                case more if guess > secret_number:
                     print ("The number is more than what I am thinking of, take another guess. ")
                case equal if guess == secret_number:
                     print ("You guessed it right, the number is, ", guess)
                     break

#ask user if they want to play again
def re_play(): 
        while True:
            play_again = str(input("Do you want to play again? y/n "))

            if play_again == "y":
                play_game()
            elif play_again == "n":
                print("Thank you for playing")
                break
            else:
                print ("Please enter a y or n")

#start the game
play_game()
re_play()
