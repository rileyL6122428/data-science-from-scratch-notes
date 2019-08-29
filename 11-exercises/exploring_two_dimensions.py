import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/06-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/07-exercises'
)
from prob import invert_normal_cdf
import random
from exploring_one_dimension_data import plot_histogram
from matplotlib import pyplot
from correlation import correlation
from my_list_matrices import shape, make_matrix, get_col

def random_normal():
    return invert_normal_cdf(random.random())

# let's make a fake data set
x_vals = [ random_normal() for _ in range(10000) ]
y_vals_1 = [ x + random_normal() / 2 for x in x_vals ]
y_vals_2 = [ -x + random_normal() / 2 for x in x_vals ]

x_and_y1_zipped = list(zip(x_vals, y_vals_1))
x_and_y2_zipped = list(zip(x_vals, y_vals_2))

def correlation_matrix(data):
    _, num_columns = shape(data)
    def matrix_entry(i, j):
        return correlation(get_col(i, data), get_col(j, data))
    return make_matrix(num_columns, num_columns, matrix_entry)

# plot_histogram(y_vals_1, .2, 'Y VALS 1')
# plot_histogram(y_vals_2, .2, 'Y VALS 1')

# pyplot.scatter(x_vals, y_vals_1, marker='.', color='blue', label='ys1')
# pyplot.scatter(x_vals, y_vals_2, marker='.', color='black', label='ys2')
# pyplot.xlabel('xs')
# pyplot.ylabel('ys')
# pyplot.legend(loc=9)
# pyplot.title('very different Joint Distributions')
# pyplot.show()

# print('correlation(x_vals, y_vals1) = %s' % correlation(x_vals, y_vals_1))
# print('correlation(x_vals, y_vals2) = %s' % correlation(x_vals, y_vals_2))

# print('correlation_matrix(x_and_y1_zipped) = %s' % (correlation_matrix(x_and_y1_zipped)))
# print('correlation_matrix(x_and_y2_zipped) = %s' % (correlation_matrix(x_and_y2_zipped)))


