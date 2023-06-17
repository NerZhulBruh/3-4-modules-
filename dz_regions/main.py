import random
import requests
import csv
import numpy as np
import matplotlib.pyplot as plt


def load_countries_name(n):
    url = 'https://randomuser.me/api/'
    params = {'results': n}
    response = requests.get(url, params=params)
    data = response.json()['results']
    countries = [user['location']['country'] for user in data]
    return countries


def generate_sales_data(num_samples, num_regions):
    city_names = load_countries_name(num_regions)
    sales_data = []

    for i in range(num_samples):
        product_id = i + 1
        sales = random.randint(1, 1000)
        region = random.choice(city_names)

        sales_data.append([product_id, sales, region])

    return sales_data


def write_sales_data(file_name, sales_data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'sales', 'sales_region'])
        writer.writerows(sales_data)


num_samples = 50
num_regions = 5

sales_data = generate_sales_data(num_samples, num_regions)

write_sales_data('result.csv', sales_data)

total_sales = 0

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sales = int(row[1])
        total_sales += sales

print("Общая сумма продаж для всех продуктов:", total_sales)

unique_regions = set()

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        region = row[2]
        unique_regions.add(region)

num_unique_regions = len(unique_regions)
print("Количество уникальных регионов продаж:", num_unique_regions)

sales_per_product = []

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sales = int(row[1])
        sales_per_product.append(sales)

average_sales_per_product = np.mean(sales_per_product)
print("Средняя сумма продаж на продукт:", average_sales_per_product)

max_sales_product = ""
max_sales_amount = 0

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product_id = row[0]
        sales = int(row[1])
        if sales > max_sales_amount:
            max_sales_amount = sales
            max_sales_product = product_id

print("Продукт с наибольшей суммой продаж:", max_sales_product)

sales_by_region = {}

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        region = row[2]
        sales = int(row[1])
        if region in sales_by_region:
            sales_by_region[region] += sales
        else:
            sales_by_region[region] = sales

plt.pie(list(sales_by_region.values()), labels=list(sales_by_region.keys()), autopct='%1.1f%%')
plt.title("Продажи по регионам")
plt.axis('equal')
plt.show()


def convert_to_rubles(sales):
    return sales * exchange_rate

exchange_rate = 70.0

data = []

with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

data_with_currency = []
data_with_currency.append(data[0] + ['currency', 'sales_in_rubles'])

for row in data[1:]:
    sales = float(row[1])
    sales_in_rubles = convert_to_rubles(sales)
    row_with_currency = row + ['RUB', sales_in_rubles]
    data_with_currency.append(row_with_currency)

with open('result_with_currency.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_with_currency)

