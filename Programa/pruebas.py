import csv

csv_file_path = r'C:\Users\franciscojavier.mart\Documents\iNews_parser\libro1.csv'
csv_data = []

with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        csv_data.append(row)

print(csv_data)