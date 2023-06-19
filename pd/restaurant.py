import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('source_data.csv')
df['date'] = pd.to_datetime(df['date'])
df_january = df.loc[df['date'].dt.month == 1]
df['day'] = df['date'].dt.date
df['hour'] = df['date'].dt.hour




# 1. У всех ли order_price == 0?
all_zero_price = (df['order_price'] == 0).all()
print(f"У всех ли order_price == 0? {all_zero_price}")

# 2. Какой процент таких заказов за весь январь?
january_orders = df[df['date'].dt.month == 1]
zero_price_percent = (january_orders['order_price'] == 0).mean() * 100
print(f"Процент заказов с ценой 0 в январе: {zero_price_percent:.2f}%")

# 3. Найти, в какие дни у нас есть заказы с ценой == 0
days_with_zero_price = df[df['order_price'] == 0]['date'].dt.date.unique()
print("Дни с заказами ценой 0:")
print(days_with_zero_price)

# 4. Топ 100 пользователей по частоте заказов
top_100_users = df['uid'].value_counts().head(100)
print("Топ 100 пользователей по частоте заказов:")
print(top_100_users)

# 5. Топ 10 пользователей, которые заказывают больше всего столовых приборов
top_10_cutlery_users = df.groupby('uid')['cutlery'].sum().nlargest(10)
print("Топ 10 пользователей по количеству заказанных столовых приборов:")
print(top_10_cutlery_users)

# 6. Топ 20 пользователей, оставивших чаевые
top_20_tipping_users = df.groupby('uid')['tips'].sum().nlargest(20)
print("Топ 20 пользователей по оставленным чаевых:")
print(top_20_tipping_users)

# 7. Топ 20 дней, когда чаевых было больше всего
top_20_days_with_high_tips = df.groupby('day')['tips'].sum().sort_values(ascending=False).head(20)
print("Топ 20 дней, когда было больше всего чаевых:")
print(top_20_days_with_high_tips)

# 8. Количество столовых приборов, пользующихся популярностью
popular_cutlery = df['cutlery'].value_counts()
print("Количество популярных столовых приборов:")
print(popular_cutlery)

# 9. Количество пользователей в данных
user_quantity = df['uid'].nunique()
print("Количество пользователей:"," {user_quantity}")

# 10. В какое время суток чаще всего осуществляют заказы
orders_by_hour = df.groupby(df['date'].dt.hour)['order_id'].count()
most_common_order_hour = orders_by_hour.idxmax()
print("Время суток, когда чаще всего осуществляют заказы:"," {most_common_order_hour} час")

plt.bar(orders_by_hour.index, orders_by_hour.values)
plt.xlabel('Время суток')
plt.ylabel('Количество заказов')
plt.title('Распределение заказов по времени суток')
plt.xticks(range(24))
plt.show()

#11
df['month'] = df['date'].dt.month
revenue_by_month = df.groupby('month')['order_price'].sum()
print("Общая выручка за все месяцы:")
print(revenue_by_month)

#12
average_tip_amount = df['tips'].mean()
print(f"Средняя сумма чаевых в заказах: {average_tip_amount:.2f}")

#13
average_cutlery_per_order = df['cutlery'].mean()
print(f"Среднее количество столовых приборов в заказе: {average_cutlery_per_order:.2f}")

#14
orders_by_day = df['day'].value_counts().nlargest(10)

plt.bar(orders_by_day.index, orders_by_day.values)
plt.xlabel('День')
plt.ylabel('Количество заказов')
plt.title('Топ-10 дней с наибольшим количеством заказов')
plt.xticks(rotation=45)
plt.show()
