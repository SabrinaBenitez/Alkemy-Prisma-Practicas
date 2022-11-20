import csv

datas = [['name', 'age'],['Bob', 14], ['Tom', 23], ['Jerry', '18']]

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)

with open("example.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(reader.line_num, row)