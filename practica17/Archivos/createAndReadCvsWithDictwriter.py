import csv

headers = ['name', 'age']
datas = [{'name':'Bob', 'age':23},
        {'name':'Jerry', 'age':44},
        {'name':'Tom', 'age':15}]

with open('example2.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    for row in datas:
        writer.writerow(row)

filename = 'example2.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['name']
        print(name)