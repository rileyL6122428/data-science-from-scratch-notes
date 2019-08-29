from code_mistakes import mistakes_per_day
from functools import reduce

def sum(list):
    return reduce(lambda x, y: x + y, list)

def mean(list):
    return sum(list) / len(list)

def is_even(list):
    return len(list) % 2 == 0

def even_median(list):
    length = len(list)
    sorted_list = sorted(list)
    left_middle_element = sorted_list[(length - 1) // 2]
    right_middle_element = sorted_list[length // 2]
    return (left_middle_element + right_middle_element) / 2

def odd_median(list):
    length = len(list)
    sorted_list = sorted(list)
    return sorted_list[length // 2]

def median(list):
    return even_median(list) if is_even(list) else odd_median(list)

# print('code_mistakes_per_day = %s' % mistakes_per_day)
# print('mean mistakes = %s' % mean(mistakes_per_day.values()))
# print('median mistakes = %s' % median(mistakes_per_day.values()))
# print('sorted mistakes values = %s' % sorted(mistakes_per_day.values())) 
