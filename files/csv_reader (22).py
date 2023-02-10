import csv

with open('data.csv', newline='') as file:
    data = csv.DictReader(file)
    print(data.fieldnames)
    for line in data:
        print(f"{line['name']:<15} -> {line['height']:^5}")

