from cleaning_and_munging_utils import try_or_none, parse_row, parse_rows_with
from dateutil import parser as date_parser
import csv

data = []
cleaned_data = []
unclean_data = []

@try_or_none
def as_float(num_string):
    return float(num_string)

@try_or_none
def as_date(date_string):
    return date_parser.parse(date_string)

with open('11-exercises/data_needing_cleaning.txt', 'r') as file:
    reader = csv.reader(file)
    for line in parse_rows_with(reader, [as_date, None, as_float]):
        data.append(line)

for row in data:
    if any(val is None for val in row):
        unclean_data.append(row)
    else:
        cleaned_data.append(row)

print('parsed_data = %s' % data)
print('cleaned_data = %s' % cleaned_data)
print('unclean_data = %s' % unclean_data)
