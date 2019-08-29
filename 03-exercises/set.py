my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
print('my_set length: %s' % len(my_set))

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)

print('item list = %s' % item_list)
print('num_items = %s' % num_items)
print('item_set = %s' % item_set)
print('num_distinct_items = %s' % num_distinct_items)
print('distinct_item_list = %s' % distinct_item_list)
