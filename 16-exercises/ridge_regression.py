import sys
sys.path.append('/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises')
sys.path.append('/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/15-exercises')
from my_list_vectors import dot_product, add_vectors
from multiple_regression import error, squared_error_gradient, estimate_beta
import random
from pokemon_trainers import trainer_party_stats, trainer_badge_counts
from stochastic_gradient_descent_two import minimize_stochastic
from functools import partial

# alpha is a 'hyperparameter' controlling how harsh the penalty is
# sometimes it's called lambda, but that already means something in le Python
def ridge_penalty(beta, alpha):
    return alpha * dot_product(beta[1:], beta[1:])

def squared_error_ridge(x_i, y_i, beta, alpha):
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)

def ridge_penalty_gradient(beta, alpha):
    return [ 0 ] + [ 2 * alpha * beta_j for beta_j in beta[1:] ]

def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
    return add_vectors(
        squared_error_gradient(x_i, y_i, beta),
        ridge_penalty_gradient(beta, alpha)
    )

def estimate_beta_ridge(xs, ys, alpha):
    beta_initial = [ random.random() for _ in range(len(xs[0])) ]

    return minimize_stochastic(
        partial(squared_error_ridge, alpha=alpha),
        partial(squared_error_ridge_gradient, alpha=alpha),
        xs,
        ys,
        beta_initial,
        0.0001
    )

random.seed(0)
trainer_beta = estimate_beta(trainer_party_stats, trainer_badge_counts)
print('trainer_beta = %s' % trainer_beta)

random.seed(0)
trainer_beta_ridge_0 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 0)
print('trainer_beta_ridge_0 = %s' % trainer_beta_ridge_0)

random.seed(0)
trainer_beta_ridge_point_01 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 0.01)
print('trainer_beta_ridge_point_01 = %s' % trainer_beta_ridge_point_01)

random.seed(0)
trainer_beta_ridge_point_1 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 0.1)
print('trainer_beta_ridge_point_1 = %s' % trainer_beta_ridge_point_1)

random.seed(0)
trainer_beta_ridge_1 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 1)
print('trainer_beta_ridge_1 = %s' % trainer_beta_ridge_1)

random.seed(0)
trainer_beta_ridge_10 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 10)
print('trainer_beta_ridge_10 = %s' % trainer_beta_ridge_10)

random.seed(0)
trainer_beta_ridge_100 = estimate_beta_ridge(trainer_party_stats, trainer_badge_counts, 100)
print('trainer_beta_ridge_100 = %s' % trainer_beta_ridge_100)


