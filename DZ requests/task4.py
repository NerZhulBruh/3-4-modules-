import requests
import datetime
r = requests.get('https://kontests.net/api/v1/sites')
now = datetime.datetime.now()
for item in r.json():
    start_date = datetime.datetime.strptime(item['start_date'], '%Y-%m-%dT%H:%M:%SZ')
    if start_date >= now and start_date <= now + datetime.timedelta(days=15):
        print(item['name'] + ' - ' + item['start_date'])
