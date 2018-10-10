import requests

#getting input
inputurl = input("Input the URL here: ").strip()
r = requests.get(inputurl)
status = r.status_code
headers = r.headers
content = r.text

print(f'The status code is: {r.status_code}')

if r.status_code is not 200:
	exit()

else:
	for key, value in headers.items():
		print(f'\n {key}: {value}')

	for line in content:
		print(line)	
