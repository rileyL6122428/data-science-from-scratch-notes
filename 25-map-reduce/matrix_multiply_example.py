from collections import defaultdict
from functools import partial
from map_reduce import map_reduce

def matrix_multiply_mapper(m, element):
    """
        m is the common dimension (columns of A, rows of B)
        element is a tuple (matrix_name, i, j, value)
    """

    name, i, j, value = element

    if name == "A":
        for k in range(m):
            yield ((i, k), (j, value))
    
    else:
        for k in range(m):
            yield((k, j), (i, value))

def matrix_multiply_reducer(m, key, indexed_values):
    results_by_index = defaultdict(list)

    for index, value in indexed_values:
        results_by_index[index].append(value)

    sum_product = sum(
        results[0] * results[1]
        for results in results_by_index.values()
        if len(results) == 2
    )

    if sum_product != 0.0:
        yield (key, sum_product)


A = [
    [3, 2, 0],
    [0, 0, 0]
]

B = [
    [4, -1, 0],
    [10, 0, 0],
    [0, 0, 0]
]

entries = [
    ("A", 0, 0, 3),
    ("A", 0, 1, 2),
    ("B", 0, 0, 4),
    ("B", 0, 1, -1),
    ("B", 1, 0, 10)
]

mapper = partial(matrix_multiply_mapper, 3)
reducer = partial(matrix_multiply_reducer, 3)

print(map_reduce(entries, mapper, reducer))
