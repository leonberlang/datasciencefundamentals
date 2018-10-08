movies = {
	"title" : "The Fast and the Furious",
	"releaseyear": 2001,
	"duration": 102,
	"director": "Rob Cohen",
}

movies["actors"] = ["Vin Diesel", "Paul Walker","Michelle Rodriguez","Jordana Brewster","Vin Diesel", "Paul Walker","Michelle Rodriguez","Jordana Brewster"]

for key, value in movies.items():
	if key == "duration": # or duration in key
		print(f'{key}: {value} minutes.')
	if key == "actors": #or actors in key
		value = ", ".join(value)
	else:
		print(f'{key}: {value}')
