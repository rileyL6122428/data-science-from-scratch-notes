import csv

with open('10-exercises/stocks_with_headers.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        date = row['date']
        company = row['company']
        closing_price = row['closing_price']
        print('date = %s, company = %s, closing_price = %s' % (date, company, closing_price))

    