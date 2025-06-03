# Create a madlibs classic word game.
#Take user input and assign them to variables

noun1 = str (input("Enter a noun: "))
noun2 = str (input("Enter another noun, preferably an animal: "))
adverb1 = str (input("Enter an adverb: "))
adverb2 = str (input("Enter another adverb: "))
adjective1 = str (input("Enter an adjective: "))
adjective2 = str (input("Enter another adjective: "))

#Generate a story that changes based on the length of the users words or their occurrence in the alphabet

if noun1 >= "5" and adverb2 > "7" and adjective1 > "5":
    print ("On a beautiful", (adjective2), "day, I went to the zoo. I saw a funny", (noun2), "swinging from the trees. Then, I spotted a majestic", (adjective2), "lion lounging in the sun.  What a wild and", (adjective1), "experience!")
elif noun2 >= "5" and adverb2 < "7" and adjective1 > "5":
    print ("On a beautiful", (adjective1), "day, I went to the zoo. I saw a funny", (noun1), "swinging from the trees. Then, I spotted a majestic", (adjective1), "lion lounging in the sun.  What a wild and", (adjective2), "experience!")