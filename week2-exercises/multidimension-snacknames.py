apes = [
	["Steyn"],
	["Nick"],
	["Yannick"]
]

for ape in apes:
	name = ape[0] 
	name_length = len(name) 
	print(name + " has a name of " + str(name_length) + " characters long.")
	snack = input(name + ", What's your fav snack? ")
	ape.append(snack) #appending them into the name string, placing it on place 1

for ape in apes:
	name = ape[0]
	print(name + " likes " + ape[1])