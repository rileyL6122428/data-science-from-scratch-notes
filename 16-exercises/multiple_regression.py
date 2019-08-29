import sys
sys.path.append('/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises')
sys.path.append('/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/15-exercises')
from my_list_vectors import dot_product
import random
from stochastic_gradient_descent_two import minimize_stochastic
from pokemon_trainers import trainer_party_stats, trainer_badge_counts
from simple_linear_regression import squared_mean_deviations

# first element of x_i should be a 1
# beta a vector of form [alpha, beta_1, beta_2, ... beta_n]
def predict(x_i, beta):
    return dot_product(x_i, beta)

def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2

def squared_error_gradient(x_i, y_i, beta):
    return [
        -2 * x_i_component * error(x_i, y_i, beta)
        for x_i_component
        in x_i
    ]

def estimate_beta(xs, ys):
    beta_initial = [ random.random() for _ in xs[0] ]

    return minimize_stochastic(
        squared_error,
        squared_error_gradient,
        xs,
        ys,
        beta_initial,
        alpha_0=0.0001
    )

# trainer_beta = estimate_beta(trainer_party_stats, trainer_badge_counts)

# print('model: (number_of_badges) = %s + (party_type_count)%s + (average_level_coeff)%s' % (beta[0], beta[1], beta[2]))
# print('alpha = %s' % beta[0])
# print('party_type_count coeff = %s' % beta[1])
# print('average_level coeff = %s' % beta[2])
    

def multiple_r_squared(xs, ys, beta):
    sum_of_squared_errors = sum(
        error(x_i, y_i, beta) ** 2
        for x_i, y_i
        in zip(xs, ys)
    )
    return 1.0 - sum_of_squared_errors / sum(squared_mean_deviations(ys))

# r_squared = multiple_r_squared(trainer_party_stats, trainer_badge_counts, beta)
# print('r_squared = %s' % r_squared)