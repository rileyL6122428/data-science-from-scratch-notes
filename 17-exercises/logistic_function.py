import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
from my_list_vectors import dot_product, add_vectors
import math
from functools import reduce
import pdb

def logistic(x):
    return 1 / (1 + math.exp(-x))

def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))

def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(
            max(logistic(dot_product(x_i, beta)), 0.0000001)
        )
    else:
        return math.log(
            max(1 - logistic(dot_product(x_i, beta)), 0.0000001)
        )
        
            

def logistic_log_likelihood(xs, ys, beta):
    return sum(
        logistic_log_likelihood_i(x_i, y_i, beta)
        for x_i, y_i
        in zip(xs, ys)
    )

def logistic_log_partial_ij(x_i, y_i, beta, j):
    return (y_i - logistic(dot_product(x_i, beta))) * x_i[j]

def logistic_log_gradient_i(x_i, y_i, beta):
    return [
        logistic_log_partial_ij(x_i, y_i, beta, j)
        for j, _
        in enumerate(beta)
    ]

def logistic_log_gradient(xs, ys, beta):
    return reduce(add_vectors, [
        logistic_log_gradient_i(x_i, y_i, beta)
        for x_i, y_i
        in zip(xs, ys)
    ])
