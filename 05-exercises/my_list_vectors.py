from functools import reduce
import math
import pdb

height_weight_age = [
    70,
    170,
    40
] # three dimensional vector

grades = [
    95, # exam1
    80, # exam2
    75, # exam3
    62  # exam4
] # four dimensional vector

# We will model vectors as lists as an example

def add_vectors(vector_a, vector_b):
    return [
        component_a + component_b
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]
    
def subtract_vectors(vector_a, vector_b):
    return [
        component_a - component_b
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

def vector_sum(vector_list):
    return reduce(add_vectors, vector_list)

def scalar_multiply(scalar, vector):
    return [
        scalar * component
        for component
        in vector
    ]

def add_nums(num1, num2):
    return num1 + num2

def vector_mean(vector):
    return reduce(add_nums, vector) / len(vector)

def component_wise_products(vector_a, vector_b):
    # pdb.set_trace()
    return [
        component_a * component_b
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

def dot_product(vector_a, vector_b):
    return reduce(add_nums, component_wise_products(vector_a, vector_b))
    # Interpreted as length of vector_a projected onto vector_b

def sum_of_squares(vector):
    return dot_product(vector, vector)

def magnitue(vector):
    return math.sqrt(sum_of_squares(vector))

def distance(vector_a, vector_b):
    return magnitue(subtract_vectors(vector_a, vector_b))

my_vector_a = [ 1, 2, 3 ]
my_vector_b = [ 4, 5, 6 ]
my_vector_c = [ 7, 8, 9 ]
# print('my vector a = %s' % my_vector_a)
# print('my vector b = %s' % my_vector_b)
# print('my vector c = %s' % my_vector_c)
# print('a + b = %s' % (add_vectors(my_vector_a, my_vector_b)))
# print('a - b = %s' % (subtract_vectors(my_vector_a, my_vector_b)))
# print('a + b + c = %s' % (vector_sum([my_vector_a, my_vector_b, my_vector_c])))
# print('5 * a = %s' % scalar_multiply(5, my_vector_a))
# print('mean: a = %s' % vector_mean(my_vector_a))
# print('a dot b = %s' % dot_product(my_vector_a, my_vector_b))
# print('a dot a (sum of squares) = %s' % sum_of_squares(my_vector_a))
# print('a magnitude = %s' % magnitue(my_vector_a))
# print('distance between a & b = %s' % distance(my_vector_a, my_vector_b))

