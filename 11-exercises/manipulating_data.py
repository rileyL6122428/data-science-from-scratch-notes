from stock_prices import stock_data
from collections import defaultdict
from functools import reduce

# Let's find the highest ever closing price for apple
# max_appl_price = max(
#     company_snapshot['closing_price']
#     for company_snapshot
#     in stock_data
#     if company_snapshot['symbol'] == 'AAPL'
# )
# print('max_appl_price = %s' % max_appl_price)

# Now let's find the max price for each company
# symbols_to_snapshots = defaultdict(list)
# for snapshot in stock_data:
#     symbols_to_snapshots[snapshot['symbol']].append(snapshot)

# symbols_to_max = {
#     symbol: max(snapshot['closing_price'] for snapshot in snapshots)
#     for symbol, snapshots
#     in symbols_to_snapshots.items()
# }
# print('symbols_to_max = %s' % symbols_to_max)


# Now let's write some utils based on the code above

def picker(field_name):
    return lambda row: row[field_name]

def pluck(field_name, rows):
    return map(picker(field_name), rows)

def group_by(grouper, rows, rows_mapper = None):
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    
    if rows_mapper:
        return {
            key: rows_mapper(rows)
            for key, rows
            in grouped.items()
        }
    else:
        return grouped

# Let rewrite our earlier examples

symbols_to_max = group_by(
    picker('symbol'),
    stock_data,
    lambda rows: max(row['closing_price'] for row in rows)
)
max_apple_closing_price = symbols_to_max['AAPL']

# print('symbols_to_max = %s' % symbols_to_max)
# print('max apple closing price = %s' % max_apple_closing_price)

# What are the largest and smallest one day percent changes in our data set?

grouped_rows = group_by(picker('symbol'), stock_data)

def percent_price_change(yesterday, today):
    return today['closing_price'] / yesterday['closing_price'] - 1

def day_over_day_changes(grouped_rows):
    grouped_and_sorted_rows = {
        symbol: sorted(rows, key=picker('date'))
        for symbol, rows
        in grouped_rows.items()
    }
    
    return {
        symbol: [
            { 
                symbol: symbol, 
                'date': today['date'], 
                'change': percent_price_change(yesterday, today)
            }
            for (yesterday, today) 
            in zip(rows, rows[1:])
        ]
        for symbol, rows
        in grouped_and_sorted_rows.items()
    }


changes_by_symbol = day_over_day_changes(grouped_rows)
print('day_over_day_changes = %s' % changes_by_symbol)

all_changes = [ 
    change
    for changes in changes_by_symbol.values()
    for change in changes
]

print('all_changes = %s' % all_changes)

max_change = max(all_changes, key=picker('change'))
print('max_change = %s' % max_change)

min_change = min(all_changes, key=picker('change'))
print('min_change = %s' % min_change)

def combine_percent_changes(change_1, change_2):
    return (1 + change_1) * (1 + change_2) - 1

def overall_change(changes):
    return reduce(combine_percent_changes, pluck('change', changes), 0)

overall_change_by_month = group_by(
    lambda row: row['date'].month,
    all_changes,
    overall_change
)

print('overall_cange_by_month = %s' % overall_change_by_month)
