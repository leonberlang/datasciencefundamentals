# Weekly Exercise 1 - Love Test Calculator

# Setting up the names (we need input) and making them comparable by cleaning them up
name1 = input("What is the first name? ").lower().strip()
name2 = input("What is the second name? ").lower().strip()

# BASIC ASSIGNMENT
#if name1 == name2:
#	print("\nJullie hebben dezelfde naam! " + name1 + (" is ook een hele goede naam ;)"))
#elif name1 > name2:
#	print(name1 + " is beter (langer) dan " + name2 + " , haha! ")
#elif name1 < name2:
#	print(name2 + " is beter (langer) dan " + name1 + " , jammer man!")
#else:
#	print("Ik weet het niet meer - error error!")

# Calculate the absolute name length to preprae for calculation.
name1_length = len(name1)
name2_length = len(name2)
namediff = name1_length - name2_length
absnamediff = abs(namediff)

#output characters
print("\nThe difference in length is " + str(absnamediff) + " characters between " + name1 + (" and ") + name2 + (".")) 

# Calculating a percentage - making sure 100% is always a full similarity. 
if name1_length > name2_length:
	namepercentage = (name2_length / name1_length * 100)
elif name1_length < name2_length:
	namepercentage = (name1_length / name2_length * 100)
else: namepercentage = ("100")

#output %
print("\nThe similarity percentage between " + name1 + " and " + name2 + " is " + str(namepercentage) + "% based on the length of the name.")

#giving the judgement 
if float(namepercentage) == 100:
	print("\n100%! A PERFECT match!")
elif float(namepercentage) >=80:
	print("\nNot bad! Go for it!")
elif float(namepercentage) >=60:
	print("\nThe match is above average!")
elif float(namepercentage) >=40:
	print("\nOk match - don't get enthousiastic about it")
elif float(namepercentage) >=20:
	print("\nThe chance is pretty small this match will work out...")
else: print("\nYou can stop now - this won't work out!")
