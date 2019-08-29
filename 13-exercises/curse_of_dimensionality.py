import random
from math import sqrt
from functools import reduce

def random_point(dimension_count):
    return [ random.random() for _ in range(dimension_count)]
# print('random 3d point = %s' % random_point(3))

def component_wise_differences(vector_a, vector_b):
    return [
        component_a - component_b
        for (component_a, component_b)
        in zip(vector_a, vector_b)
    ]
# print('component_wise_differences([1, 1], [1, 2] = %s' % component_wise_differences([1, 1], [1, 2]))

def distance(vector_a, vector_b):
    differences = component_wise_differences(vector_a, vector_b)
    squared_differences = [ difference ** 2 for difference in differences]
    squared_differences_sum = reduce(lambda accum, next: accum + next, squared_differences)
    return sqrt(squared_differences_sum)
# print('disance([1, 1], [4, 5]) = %s' % distance([1, 1], [4, 5]))

# takes a number of dimensions & number of random pairs
# produces a list of random distances between random points
def random_distances(dimension_total, distances_total):
    return [
        distance(random_point(dimension_total), random_point(dimension_total))
        for _
        in range(distances_total)
    ]

def average(vector):
    return sum(vector) / len(vector)

for number in range(1000):
    dimension = number + 1
    print('random_distances(%s, 10) = %s' % (dimension, average(random_distances(dimension, 10))))