import csv
import json
from pprint import pprint


with open('rate.json') as f:
    data = json.load(f)
# pprint(data)
new_data = []
for key in data['Valute'].keys():
    item = data['Valute'][key]
    new_data.append((item['CharCode'], item['Name']))
new_data.sort()
print(new_data)
with open('task5.csv', mode='w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['CharCode', 'Name'])
    writer.writerows(new_data)
print(new_data.index(('USD', 'Доллар США')) + 2)
