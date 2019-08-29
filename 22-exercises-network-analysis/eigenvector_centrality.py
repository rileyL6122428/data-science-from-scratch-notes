import random
from functools import partial
import sys
sys.path.append('/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises')

from my_list_vectors import dot_product, magnitue, distance, scalar_multiply
from my_list_matrices import shape, get_row, get_col, make_matrix

from fb_friend_data import users, friendships
import pdb

def matrix_product_entry(A, B, i, j):
    return dot_product(get_row(i, A), get_col(j, B))

def matrix_multiply(A, B):
    n1, k1 = shape(A)
    n2, k2 = shape(B)

    if k1 != n2:
        raise ArithmeticError('Incompatible Matrix Shapes!')

    return make_matrix(n1, k2, partial(matrix_product_entry, A, B))
    
def vector_as_matrix(vector):
    return [
        [ component ]
        for component
        in vector
    ]

def vector_from_matrix(vector_as_matrix):
    return [
        row[0]
        for row
        in vector_as_matrix
    ]

def matrix_operate(A, v):
    v_as_matrix = vector_as_matrix(v)
    product = matrix_multiply(A, v_as_matrix)
    return vector_from_matrix(product)

def find_eigenvector(A, tolerance=0.00001):
    guess = [ random.random() for _ in A ]

    while True:
        result = matrix_operate(A, guess)
        length = magnitue(result)
        next_guess = scalar_multiply(1 / length, result)

        if distance(guess, next_guess) < tolerance:
            eigenvector, eigenvalue = next_guess, length
            return eigenvector, eigenvalue
        else:
            guess = next_guess

def entry_fn(node_i, node_j):
    return 1 if (node_i, node_j) in friendships or (node_j, node_i) in friendships else 0

adjacency_matrix_dimension = len(users)
friendships_adjacency_matrix = make_matrix(
    adjacency_matrix_dimension,
    adjacency_matrix_dimension,
    entry_fn
)
# pdb.set_trace()
eigenvector_centralities, _ = find_eigenvector(friendships_adjacency_matrix)
print(eigenvector_centralities)
        