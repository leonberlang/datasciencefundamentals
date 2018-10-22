"""
To see an example of the Wikipedia API JSON look at this url:
https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
"""
import requests

def wikilookup(title, value):
	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
	req = requests.get(url)
	if req.status_code != 200:
		print(f'We got an error: {req.status_code}')
		exit()
	data = req.json()
	return data[f"{value}"]

title = input("Article name?: ").strip().lower()
value = input("Value: ").strip().lower()	

data = wikilookup(title, value)

print(f"Here is the {value} for {title}:")
print(data)
