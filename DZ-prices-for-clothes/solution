from requests import get
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/exercise/list_basic/'
for i in range(1, 7):
  params = {'page': i}
  response = get(url, params=params)
  soup = BeautifulSoup(response.text, 'html.parser')
  items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
  for item in items:
    title = item.find('h4', class_='card-title').text.strip('\n')
    price =  item.find('h5').text
    print(  title ,':', price)
