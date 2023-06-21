import requests
from bs4 import BeautifulSoup

url = 'https://emojipedia.org/search/'

categories = ["nature", "music", "science", "food", "sports"]

for category in categories:
    params = {'q': category}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find('ol', class_='search-results')

    if elements:
        items = elements.find_all('a')
        all_emojis = [item.text for item in items]
        quantity = len(all_emojis)
        print('{} содержит {} эмоджи.'.format(category, quantity))
        print(all_emojis)
    else:
        print('На странице не найдены эмоджи для категории {}.'.format(category))
