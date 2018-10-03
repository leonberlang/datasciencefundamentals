friends = ["Henk", "Jaap", "Kees"] #, "Herman", "Jasper", "Luuk", "Steyn", "Nick"
snacklist = []
for name in friends:
	print(name)
	name_length = len(name)
	print(str(name_length) + " characters long")
	snack = input(name + ", What is your fav snack?")
	snacklist.append(snack)

index = 0

for name in friends:
	print(name)
	print(index)
	print(snacklist[index]) #wat tussen [] staat is het nummer in de lijst, en daar kan je controle uitoefenen via zelf daar steeds eentje bij toe te voegen
	index =  index + 1 #moet eerst printen anders begin je al bij EEN
	
# if u use for the variable after that is new and created
# can also just make varaible snack = snacklist[index]
