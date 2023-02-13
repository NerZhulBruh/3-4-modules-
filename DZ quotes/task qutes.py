import requests
from bs4 import BeautifulSoup


def get_quotes():
    page = 1
    while True:
        url = 'http://quotes.toscrape.com/page/' + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        for i in range(len(quotes)):
            print(f'{quotes[i].get_text()} - {authors[i].get_text()}')
        next_btn = soup.find('li', class_='next')
        if not next_btn:
            break
        page += 1
print(get_quotes())
