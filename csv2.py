import csv

with open ('answers.csv', 'r', encoding='utf-8') as file:
    fields = ['inc_mes', 'out_mes']
    reader = csv.DictReader(file, fields, delimiter = ';')

    for row in reader:
        print(row)