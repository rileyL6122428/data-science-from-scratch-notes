# We will use 2 dimensional array to represent matrices
# matix names are usually in caps


def num_rows(matrix):
    return len(matrix)

def num_cols(matrix):
    return len(matrix[0])

def shape(matrix):
    return num_rows(matrix), num_cols(matrix)

def get_row(row_index, matrix):
    return matrix[row_index]

def get_col(col_index, matrix):
    return [
        matrix[row_index][col_index]
        for row_index
        in range(num_rows(matrix))
    ]

def make_matrix(num_rows, num_cols, entry_function):
    return [
        [
            entry_function(row_index, col_index)
            for col_index in range(num_cols)
        ]
        for row_index in range(num_rows)
    ]

def identity_generation(row_index, col_index):
    return 1 if row_index == col_index else 0

def identity_matrix(num_rows, num_cols):
    return make_matrix(num_rows, num_cols, identity_generation)

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# print('A = %s' % A)
# print('B = %s' % B)
# print('A num of rows = %s' % num_rows(A))
# print('A num of cols = %s' % num_cols(A))
# print('A row 0 = %s' % get_row(0, A))
# print('A col 0 = %s' % get_col(0, A))
# print('make 2x2 matrix with index sums = %s' % make_matrix(2, 2, lambda x, y: x + y))
# print('make 3x3 identity matrix = %s' % identity_matrix(3, 3))