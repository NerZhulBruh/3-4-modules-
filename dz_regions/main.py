import requests
import numpy as np
import csv
import matplotlib.pyplot as plt
from collections import Counter

def generate_random_regions(num_regions):
    url = 'https://randomuser.me/api/'
    params = {'results': num_regions}
    response = requests.get(url, params=params)
    data = response.json()['results']
    regions = [user['location']['country'] for user in data]
    return regions

currency_codes = {
    'Libya': 'LYD',
 'South Sudan': 'SSP',
 'Syria': 'SYP',
 'Venezuela': 'VES',
 'Yemen': 'YER',
 'Zimbabwe': 'ZWL',
 'United Arab Emirates': 'AED',
 'Afghanistan': 'AFN',
 'Albania': 'ALL',
 'Armenia': 'AMD',
 'Netherlands Antilles': 'ANG',
 'Angola': 'AOA',
 'Argentina': 'ARS',
 'Australia': 'AUD',
 'Aruba': 'AWG',
 'Azerbaijan': 'AZN',
 'Bosnia and Herzegovina': 'BAM',
 'Barbados': 'BBD',
 'Bangladesh': 'BDT',
 'Bulgaria': 'EUR',
 'Bahrain': 'BHD',
 'Burundi': 'BIF',
 'Bermuda': 'BMD',
 'Brunei': 'BND',
 'Bolivia': 'BOB',
 'Brazil': 'BRL',
 'Bahamas': 'BSD',
 'Bhutan': 'BTN',
 'Botswana': 'BWP',
 'Belarus': 'BYN',
 'Belize': 'BZD',
 'Canada': 'CAD',
 'Democratic Republic of the Congo': 'CDF',
 'Switzerland': 'CHF',
 'Chile': 'CLP',
 'China': 'CNY',
 'Colombia': 'COP',
 'Costa Rica': 'CRC',
 'Cuba': 'CUP',
 'Cape Verde': 'CVE',
 'Czech Republic': 'CZK',
 'Djibouti': 'DJF',
 'Denmark': 'EUR',
 'Dominican Republic': 'DOP',
 'Algeria': 'DZD',
 'Egypt': 'EGP',
 'Eritrea': 'ERN',
'Ethiopia': 'ETB',
 'European Union': 'EUR',
 'Fiji': 'FJD',
 'Falkland Islands': 'FKP',
 'Faroe Islands': 'FOK',
 'United Kingdom': 'GBP',
 'Georgia': 'GEL',
 'Guernsey': 'GGP',
 'Ghana': 'GHS',
 'Gibraltar': 'GIP',
 'The Gambia': 'GMD',
 'Guinea': 'GNF',
 'Guatemala': 'GTQ',
 'Guyana': 'GYD',
 'Hong Kong': 'HKD',
 'Honduras': 'HNL',
 'Croatia': 'EUR',
 'Haiti': 'HTG',
 'Hungary': 'EUR',
 'Indonesia': 'IDR',
 'Israel': 'ILS',
 'Isle of Man': 'IMP',
 'India': 'INR',
 'Iraq': 'IQD',
 'Iran': 'IRR',
 'Iceland': 'ISK',
 'Jersey': 'JEP',
 'Jamaica': 'JMD',
 'Jordan': 'JOD',
 'Japan': 'JPY',
 'Kenya': 'KES',
 'Kyrgyzstan': 'KGS',
 'Cambodia': 'KHR',
 'Kiribati': 'KID',
 'Comoros': 'KMF',
 'South Korea': 'KRW',
 'Kuwait': 'KWD',
 'Cayman Islands': 'KYD',
 'Kazakhstan': 'KZT',
 'Laos': 'LAK',
 'Lebanon': 'LBP',
 'Sri Lanka': 'LKR',
 'Liberia': 'LRD',
 'Lesotho': 'LSL',
 'Morocco': 'MAD',
 'Moldova': 'MDL',
 'Madagascar': 'MGA',
 'North Macedonia': 'MKD',
'Myanmar': 'MMK',
 'Mongolia': 'MNT',
 'Macau': 'MOP',
 'Mauritania': 'MRU',
 'Mauritius': 'MUR',
 'Maldives': 'MVR',
 'Malawi': 'MWK',
 'Mexico': 'MXN',
 'Malaysia': 'MYR',
 'Mozambique': 'MZN',
 'Namibia': 'NAD',
 'Nigeria': 'NGN',
 'Nicaragua': 'NIO',
 'Norway': 'NOK',
 'Nepal': 'NPR',
 'New Zealand': 'NZD',
 'Oman': 'OMR',
 'Panama': 'PAB',
 'Peru': 'PEN',
 'Papua New Guinea': 'PGK',
 'Philippines': 'PHP',
 'Pakistan': 'PKR',
 'Poland': 'EUR',
 'Paraguay': 'PYG',
 'Qatar': 'QAR',
 'Romania': 'EUR',
 'Serbia': 'RSD',
 'Russia': 'RUB',
 'Rwanda': 'RWF',
 'Saudi Arabia': 'SAR',
 'Solomon Islands': 'SBD',
 'Seychelles': 'SCR',
 'Sudan': 'SDG',
 'Sweden': 'EUR',
 'Singapore': 'SGD',
 'Saint Helena': 'SHP',
 'Sierra Leone': 'SLE',
 'Somalia': 'SOS',
 'Suriname': 'SRD',
 'São Tomé and Príncipe': 'STN',
 'Eswatini': 'SZL',
 'Thailand': 'THB',
'Tajikistan': 'TJS',
 'Turkmenistan': 'TMT',
 'Tunisia': 'TND',
 'Tonga': 'TOP',
 'Turkey': 'TRY',
 'Trinidad and Tobago': 'TTD',
 'Tuvalu': 'TVD',
 'Taiwan': 'TWD',
 'Tanzania': 'TZS',
 'Ukraine': 'UAH',
 'Uganda': 'UGX',
 'United States': 'USD',
 'Uruguay': 'UYU',
 'Uzbekistan': 'UZS',
 'Vietnam': 'VND',
 'Vanuatu': 'VUV',
 'Samoa': 'WST',
 'CEMAC': 'XAF',
 'Organisation of Eastern Caribbean States': 'XCD',
 'International Monetary Fund': 'XDR',
 'CFA': 'XOF',
 "Collectivités d'Outre-Mer": 'XPF',
 'South Africa': 'ZAR',
 'Zambia': 'ZMW',
 'Austria': 'EUR',
 'Belgium': 'EUR',
 'Cyprus': 'EUR',
 'Czechia': 'EUR',
 'Estonia': 'EUR',
 'Finland': 'EUR',
 'France': 'EUR',
 'Germany': 'EUR',
 'Greece': 'EUR',
 'Ireland': 'EUR',
 'Italy': 'EUR',
 'Latvia': 'EUR',
 'Lithuania': 'EUR',
 'Luxembourg': 'EUR',
 'Malta': 'EUR',
 'Netherlands': 'EUR',
 'Portugal': 'EUR',
 'Slovakia': 'EUR',
 'Slovenia': 'EUR',
 'Spain': 'EUR'
}

def get_currency_code(country):
    return currency_codes.get(country, "Unknown")

def get_exchange_rate():
    response = requests.get("https://open.er-api.com/v6/latest/RUB")
    data = response.json()
    rates = data.get("rates", {})
    exchange_rate = rates.get("RUB")
    return exchange_rate

def convert_to_rubles(amount, currency, exchange_rate):
    if currency == "Unknown":
        return "Unknown"
    else:
        return round(amount * exchange_rate, 2)

np.random.seed(42)
ids = np.arange(1, 51)
sales = np.random.randint(10, 100, size=50)
sales_regions = generate_random_regions(5)


sales_data = []
for i in range(len(ids)):
    country = sales_regions[i % len(sales_regions)] 
    currency = get_currency_code(country)
    exchange_rate = get_exchange_rate()
    sales_rub = convert_to_rubles(sales[i], currency, exchange_rate)
    sales_data.append({
        "ID": ids[i],
        "Sales": sales[i],
        "Sales Region": sales_regions[i % len(sales_regions)],  
        "Currency": currency,
        "Sales (RUB)": sales_rub
    })

filename = "sales_data.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Sales", "Sales Region", "Currency", "Sales (RUB)"])
    total_sales = 0  
    unique_regions = set()  
    sales_per_product = []  
    top_products = Counter()  
    for sale in sales_data:
        writer.writerow([sale["ID"], sale["Sales"], sale["Sales Region"], sale["Currency"], sale["Sales (RUB)"]])
        total_sales += sale["Sales"]
        unique_regions.add(sale["Sales Region"])
        sales_per_product.append(sale["Sales"])
        top_products[sale["ID"]] += sale["Sales"]

    writer.writerow([])
    writer.writerow(["Task", "Result"])
    writer.writerow(["Всего продаж", total_sales])
    writer.writerow(["Уникальных регионов", len(unique_regions)])
    writer.writerow(["Средние продажи", np.mean(sales_per_product)])
    writer.writerow(["Самый дорогой продукт", top_products.most_common(1)[0][0]])
    writer.writerow([]) 
    writer.writerow(["Продажи по регионам"])
    region_sales = Counter()
    for sale in sales_data:
        region_sales[sale["Sales Region"]] += sale["Sales"]
    for region, sales in region_sales.items():
        writer.writerow([region, sales])


plt.figure(figsize=(8, 8))
regions, sales = zip(*region_sales.items())
plt.pie(sales, labels=regions, autopct="%1.1f%%")
plt.title("Sales per Region")
plt.savefig("sales_per_region.png")
plt.close()

top_products = top_products.most_common(5)
top_products_names = [f"Product {product[0]}" for product in top_products]
top_products_sales = [product[1] for product in top_products]
other_sales = total_sales - sum(top_products_sales)
top_products_names.append("Other")
top_products_sales.append(other_sales)

plt.figure(figsize=(8, 8))
plt.pie(top_products_sales, labels=top_products_names, autopct="%1.1f%%")
plt.title("Top 5 Products by Sales")
plt.savefig("top_5_products.png")
plt.close()

print("Результат в файле:", filename)

