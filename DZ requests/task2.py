import requests
def convert(amount, from_currency, to_currency):
    url = 'https://open.er-api.com/v6/latest/{}'.format(from_currency)
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    result = amount * rate
    return result

amount = float(input('Введите сумму для конвертации: '))
from_currency = input('Введите исходную валюту (USD, RUB, EUR): ').upper()
to_currency = input('Введите конечную валюту (USD, RUB, EUR): ').upper()
converted_amount = convert(amount, from_currency, to_currency)
print('{} {} равно {} {}'.format(amount, from_currency, converted_amount, to_currency))
