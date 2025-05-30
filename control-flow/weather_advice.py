#App to provide clothing recommendations to user based on user input
#Suggest weather conditions from input

current_weather = str(input("What's the weather like today? (sunny/rainy/cold):"))

#Assign suggestions based on weather conditions

if current_weather == str("sunny"):
    print("Wear a t-shirt and sunglasses.")
elif current_weather == str("rainy"):
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == str("cold"):
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I dont have recommendations for this weather.")