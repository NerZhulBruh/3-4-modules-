import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Страна': ['США', 'США', 'США', 'Китай', 'Китай', 'Китай', 'Германия', 'Германия', 'Германия'],
    'Год': [2010, 2011, 2012, 2010, 2011, 2012, 2010, 2011, 2012],
    'Объем': [500, 550, 600, 450, 520, 590, 400, 420, 440]
}

with open('countries.csv', 'w', encoding='utf-8') as file:
    headers = ['Страна', 'Год', 'Объем']
    file.write(','.join(headers) + '\n')
    for i in range(len(data['Страна'])):
        row = [data['Страна'][i], str(data['Год'][i]), str(data['Объем'][i])]
        file.write(','.join(row) + '\n')

df = pd.read_csv('countries.csv')

plt.figure(figsize=(8, 6))
colors = ['k', 'r', 'purple']

for country, color in zip(df['Страна'].unique(), colors):
    country_data = df[df['Страна'] == country]
    plt.plot(country_data['Год'], country_data['Объем'], marker='x', color=color, label=country)

plt.xticks(range(2010, 2013))  
plt.yticks(range(400, 651, 50))
plt.xlabel('Год')
plt.ylabel('Объем торговли')
plt.title('Объем торговли по странам и годам')
plt.legend()

with open('graphics.png', 'wb') as file:
    plt.savefig(file, format='png')
