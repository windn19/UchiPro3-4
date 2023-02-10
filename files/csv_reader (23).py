import csv

with open('data.csv', newline='') as file:
    names = ['name', 'height', 'mass', 'hair_color', 'skin_color']
    data = csv.DictReader(file, fieldnames=names)
    print(data.fieldnames)
    for line in data:
        print(f"{line['name']:<15} -> {line['height']:^5}")
