import requests
url = 'https://official-joke-api.appspot.com/jokes/ten'
response = requests.get(url)
data = response.json()
types_of_jokes = [item['type'] for item in data]
print(types_of_jokes)
