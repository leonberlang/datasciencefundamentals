import requests
import json

#getting initial input
inputdata = input("Article name: ").lower().strip().replace(" ","_")
inputurl = f"https://en.wikipedia.org/api/rest_v1/page/summary/{inputdata}"
req = requests.get(inputurl)
statuscode = req.status_code

#notifying user if something goes wrong
if statuscode is not 200:
	print(f'something went wrong... error code: {statuscode}')
	exit()

#convert data into json dictionary
data = json.loads(req.text)

#setting up prefix and the full langauges
langs = ["en.","it.","nl.","es."]
langsfull = ["English","Italian","Dutch","Spanish"]

for lang in langs:
	location = langs.index(lang)
	inputnew = inputurl.replace("en.",lang) #could also just use prefix but have to do that at line 6 already
	req = requests.get(inputnew)
	data = json.loads(req.text)
	print(f"\nLangauge: {langsfull[location]}")
	print(f"\nTitle: {data['title']}")
	if "description" not in data:
		print(f"Description: No description exists.")
	else:
		print(f"\nDescription: {data['description']}")
	if "extract" not in data: 
		print("No extract exists.")
	else:
		print(f"\nExtract: {data['extract']}")

# beter om nog om te zetten naar key + value
# value checken of hij leeg is
