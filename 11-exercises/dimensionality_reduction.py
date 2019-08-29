import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/09-exercises'
)
from maximize_utils import maximize_batch
import math
from dimensionality_reduction_data import sample_data
from functools import reduce, partial
import pdb

def shape(A):
    return len(A), len(A[0])

def component_means(vectors):
    vector_total, component_total = len(vectors), len(vectors[0])
    component_means = [ 0 for _ in range(component_total)]
    for vector in vectors:
        for index, component in enumerate(vector):
            component_means[index] += component / vector_total
    return component_means

def make_matrix(original, transform):
    new_matrix = []
    for row_idx, _ in enumerate(original):
        new_matrix.append([])
        for col_idx, _ in enumerate(original[row_idx]):
            new_matrix[row_idx].append(transform(row_idx, col_idx))
    return new_matrix

def component_std_devs(vectors):
    vector_total, component_total = len(vectors), len(vectors[0])
    means = component_means(vectors)
    mean_devs_squared =  make_matrix(vectors, lambda row, col: (vectors[row][col] - means[col]) ** 2)
    component_variances = [ 0 for _ in range(component_total) ]
    for vector in mean_devs_squared:
        for index, mean_dev_squared in enumerate(vector):
            component_variances[index] += mean_dev_squared / vector_total
    component_std_devs = list(map(lambda num: math.sqrt(num), component_variances))
    return component_std_devs

def scale(vectors):
    return component_means(vectors), component_std_devs(vectors)

def de_mean_matrix(A):
    number_of_rows, number_of_cols = shape(A)
    column_means, _ = scale(A)
    return make_matrix(A, lambda row, col: A[row][col] - column_means[col])


de_meaned_data = de_mean_matrix(sample_data)

def vector_magnitude(vector):
    squared_sum = reduce(lambda accum, term: accum + term ** 2, vector, 0)
    return math.sqrt(squared_sum)

def direction_vector(vector):
    magnitude = vector_magnitude(vector)
    return [ component / magnitude for component in vector ]

def component_wise_products(vector_a, vector_b):
    component_pairs = zip(vector_a, vector_b)
    return list(map(lambda num_pair: num_pair[0] * num_pair[1], component_pairs))

def dot_product(vector_a, vector_b):
    a_b_component_products = component_wise_products(vector_a, vector_b)
    return reduce(lambda accum, next: accum + next, a_b_component_products)

def directional_variance(vector, contrast_vector):
    return dot_product(vector, direction_vector(contrast_vector)) ** 2

def directional_variance_composite(vector_list, contrast_vector):
    return sum(
        directional_variance(vector, contrast_vector)
        for vector
        in vector_list
    )

def directional_variance_gradient(vector, contrast_vector):
    projection_length = dot_product(vector, direction_vector(contrast_vector))
    return [
        2 * projection_length * component
        for component 
        in vector
    ]

def component_sum(vectors, index):
    return reduce(lambda accum, next: accum + next[index], vectors, 0)

def vector_sum(vectors):
    return [
        component_sum(vectors, component_index)
        for component_index
        in range(len(vectors[0]))
    ]

def directional_variance_gradient_composite(vector_list, contrast_vector):
    return vector_sum([
        directional_variance_gradient(vector, contrast_vector)
        for vector
        in vector_list
    ])

# First principal component is the direction that maximizes the
# directional variance function.
def first_principal_component(vector_list):
    guess = [1 for _ in vector_list[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance_composite, vector_list),
        partial(directional_variance_gradient_composite, vector_list),
        guess
    )
    maximized_direction = direction_vector(unscaled_maximizer)
    return maximized_direction

def scalar_multiply(scalar, vector):
    return map(lambda component: component * scalar, vector);

def project(vector, other_vector):
    projection_length = dot_product(vector, other_vector)
    return scalar_multiply(projection_length, other_vector)

