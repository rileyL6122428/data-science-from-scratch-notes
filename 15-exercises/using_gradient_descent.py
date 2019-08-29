import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/09-exercises'
)
from simple_linear_regression import error
import random
from pokemon_trainer_data import trainer_pokemon_counts, trainer_win_counts
from stochastic_gradient_descent import minimize_stochastic

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i)

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta, = theta
    return [
        -2 * error(alpha, beta, x_i, y_i),      # alpha partial derivative
        -2 * error(alpha, beta, x_i, y_i) * x_i # beta partial derivative
    ]

random.seed(0)
theta = [ random.random(), random.random() ]
alpha, beta = minimize_stochastic(
    squared_error,
    squared_error_gradient,
    trainer_pokemon_counts,
    trainer_win_counts,
    theta,
    0.0000001
)
# print('with minimize stochastic')
# print('trainer_alpha = %s, trainer_beta = %s' % (alpha, beta))