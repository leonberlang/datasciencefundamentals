import json

# with open("movies.json") as f:
#movies = json.load(f)

f = open("movies.json")
movies = json.load(f) #more readable version in the variable movies

yearinput = input("What year needs to be the film out of? ").strip()
yearinput = int(yearinput)

# checken of de key al bestaat (de filmmaker)
# anders in dictionary de key aanmaken en dan de value +1
# sorteren op basis van een waarde (volgende week)

for movie in movies:
	year = movie["year"]
	title = movie["title"]
	if year == yearinput:
		print(title)

print("Other filtering options are:")
print("- Movies longer than a certain DURATION.")
print("- Movies where the DIRECTOR is also an actor.")
print("- Movies that the director is also an actor.")
question = input("\nEnter the keyword: ")
if question == "DURATION":
	filmduration = int(input("The film has to be longer than what duration? "))
	for movie in movies:
		duration = movie["duration"]
		title = movie["title"]
		if duration >= filmduration:
			print(title)

if question == "DIRECTOR":
	print("In the following movies the director is also an actor:\n")
	for movie in movies:
		director = movie["director"]
		actors = movie["actors"]
		title = movie["title"]
		if director in actors:
			print(title)

if question == "SPECIFIC":
		directorinput = input("What director? ")
		for movie in movies:
			director = movie["director"]
			title = movie["title"]
			if director == directorinput:
				print(title)	
