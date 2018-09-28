#Calculating nutritions per single chip instead of 16 chips (1 serving)
defserving = 16
pringles_calories = 150/defserving
pringles_carbohydrate = 15/defserving
pringles_fat = 9/defserving
pringles_sodium = .15/defserving

servingsize = input("Enter the amount of chips here: ")
servingsize = float(servingsize)

calculated_pringles_calories = servingsize * pringles_calories
calculated_pringles_carbohydrate = servingsize * pringles_carbohydrate
calculated_pringles_fat = servingsize * pringles_fat
calculated_pringles_sodium = servingsize * pringles_sodium

print("If you want to eat " + str(servingsize) + " chips" + " you will be consuming the following nutritions:")
print(str(calculated_pringles_calories) + " calories")
print(str(calculated_pringles_carbohydrate) + " grams of carbohydrate")
print(str(calculated_pringles_fat) + " grams of fat")
print(str(calculated_pringles_sodium) + " grams of sodium")

#single print command, trying out the \n new line function
print("\n Everything at once:\n" + "\n" + str(calculated_pringles_calories) + " calories" 
      + "\n" + str(calculated_pringles_carbohydrate) + " grams of carbohydrate"
      + "\n" + str(calculated_pringles_fat) + " grams of fat"
      + "\n" + str(calculated_pringles_sodium) + " grams of sodium")

