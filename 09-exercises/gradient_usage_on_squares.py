from basic_idea_grad_descent import sum_of_squares, partial_difference_quotient, estimate_gradient
import random
from functools import reduce
from math import sqrt

# let's try to minimze the sum of squares function for three dimensional vectors
def step(vector, direction, step_size):
    return [
        vect_component + step_size * direction_i
        for vect_component, direction_i
        in zip(vector, direction)
    ]

def sum_of_squares_gradient(vector):
    return [ 2 * vect_component for vect_component in vector ]

def squared_differences(vector_a, vector_b):
    return [
        (component_a - component_b) ** 2
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

def distance(vector_a, vector_b):
    return sqrt(sum(squared_differences(vector_a, vector_b)) / len(vector_a))

my_vector = [ random.randint(-10, 10) for _ in range(3) ]

tolerance = 0.0000001

while True:
    print('my vector = %s' % my_vector)
    gradient = sum_of_squares_gradient(my_vector)
    next_vector = step(my_vector, gradient, -0.01)
    if distance(next_vector, my_vector) < tolerance:
        break
    else:
        my_vector = next_vector

print('final vector = %s' % my_vector)    