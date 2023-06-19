import random
import requests
import json
import csv
import pandas as pd

def generate_ids(data_len):
    ids = [str(random.randint(0, 99999)) for _ in range(data_len)]
    return ids

def generate_salary(data_len):
    salary = [str(random.randint(100000, 999999)) for _ in range(data_len)]
    return salary

def generate_month(data_len):
    months = [str(random.randint(1, 12)) for _ in range(data_len)]
    return months

def generate_users(data_len):
    url = "https://randomuser.me/api/"
    params = {'results': data_len}
    response = requests.get(url, params=params)
    data = response.json()
    results = data['results']
    names = [result['name']['first'] for result in results]
    return names

def write_data(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Salary', 'Month', 'User'])
        writer.writerows(data)

data_len = 15
ids = generate_ids(data_len)
salary = generate_salary(data_len)
months = generate_month(data_len)
users = generate_users(data_len)

data = list(zip(ids, salary, months, users))
file_name = 'users_data.csv'
write_data(file_name, data)

def find_average_salary(file_name):
    df = pd.read_csv(file_name)
    salary_column = df['Salary']
    average_salary = salary_column.mean()
    return average_salary

file_name = 'users_data.csv'
average_salary = find_average_salary(file_name)
print("Средняя зарплата: {}".format(average_salary))
