apes = {
	"Steyn": "",
 	"Nick": "",
 	"Mateu": "",
 	"Yannick": ""
}

for ape, food in apes.items():
	print(f'{ape} is {len(ape)} characters long.') 
	snack = input(f'{ape}, what is your fav snack? ')
	add = apes[ape] = snack
	# can also make a list and add new dictionaries to that with multiple values
	# like length etc. not limiting

for ape, food in apes.items():
	print(f'{ape} likes {food} and has a name length of {len(ape)}.')
