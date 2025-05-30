#App to provide clothing recommendations to user based on user input
#Suggest weather conditions from input

weather = str(input("What's the weather like today? (sunny/rainy/cold):"))

#Assign suggestions based on weather conditions

if weather == str("sunny"):
    print("Wear a t-shirt and sunglasses.")
elif weather == str("rainy"):
    print("Don't forget your umbrella and a raincoat.")
elif weather == str("cold"):
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I dont have recommendations for this weather.")