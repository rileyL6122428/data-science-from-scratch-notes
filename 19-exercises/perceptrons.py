import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
from my_list_vectors import dot_product

def step_function(weighted_sum):
    return 1 if weighted_sum  >= 0 else 0

def perceptron_output(weights, bias, inputs):
    weighted_sum = dot_product(weights, inputs) + bias
    return step_function(weighted_sum)

