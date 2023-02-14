import requests
url = 'https://api.publicapis.org/entries'
response = requests.get(url)
data = response.json()
oauth_count = 0
total_count = 0
for entry in data['entries']:
    if 'Auth' in entry and entry['Auth'] == 'OAuth':
        oauth_count += 1
    total_count += 1
print('Процентное соотношение OAuth аутентификации к общему числу публичных API: {}%'.format(oauth_count/total_count * 100))

github_count = 0
for entry in data['entries']:
    if 'Link' in entry and 'github' in entry['Link']:
        github_count += 1
print('Количество API, развернутых на GitHub: {}'.format(github_count))

categories = {}
for entry in data['entries']:
    if 'Category' in entry and entry['Category'] not in categories:
        categories[entry['Category']] = 1
    elif 'Category' in entry and entry['Category'] in categories:
        categories[entry['Category']] += 1
print('Количество публичных API в каждой категории:')
for category, count in categories.items():
    print('{}: {}'.format(category, count))
