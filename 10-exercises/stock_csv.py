import csv

# 'rb' is read binary
with open('10-exercises/stocks.txt', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        date = row[0]
        company = row[1]
        price = row[2]
        print('date = %s, company = %s, price = %s' % (date, company, price))