from heights_and_weights import body_proportions
from collections import defaultdict
from functools import reduce
import math

def get_mean(vals):
    return reduce(lambda num1, num2: num1 + num2, vals) / len(vals)

def get_mean_deviations_squared(vals):
    mean = get_mean(vals)
    return map(lambda val: (val - mean) ** 2, vals)

def add(val_a, val_b):
    return val_a + val_b

def get_variance(vals):
    return reduce(add, get_mean_deviations_squared(vals)) / len(vals)

def get_standard_deviation(vals):
    return math.sqrt(get_variance(vals))

def get_keys(rows):
    return [
        key
        for key, _
        in rows[0].items()
    ]

def group_by_attribute(rows):
    keys = get_keys(rows)
    cols = defaultdict(list)
    for key in keys:
        for row in rows:
            cols[key].append(row[key])
    return cols

def scale(data):
    grouped_by_attribute = group_by_attribute(data)

    means = {
        attribute_name: get_mean(grouped_by_attribute[attribute_name])
        for attribute_name
        in grouped_by_attribute.keys()
    }

    standard_deviations = {
        attribute_name: get_standard_deviation(grouped_by_attribute[attribute_name])
        for attribute_name
        in grouped_by_attribute.keys()
    }

    return means, standard_deviations

def rescale(data):
    means, stdevs = scale(data)

    def rescaled(key, value):
        return (value - means[key]) / stdevs[key] if stdevs[key] != 0 else value

    return [
        {
            key: rescaled(key, value)
            for key, value in sample.items()
        }
        for sample in data
    ]


print('body_proportions = %s' % body_proportions)
print('rescaled(body_proportions) = %s' % rescale(body_proportions))
# ON PAGE 194

