import json

f = open("movies.json")
movies = json.load(f) #more readable version in the variable movies

yearinput = int(input("What year needs to be the film out of? ")).strip()

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
