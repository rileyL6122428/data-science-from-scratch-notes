import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/06-exercises'
)
from correlation import correlation
from dispersion import standard_deviation
from central_tendencies import mean
from pokemon_trainer_data import trainers, trainer_pokemon_counts, trainer_win_counts

# Simple Linear Regression functions

def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, xs, ys):
    return sum(
        error(alpha, beta, x_i, y_i) ** 2
        for x_i, y_i
        in zip(xs, ys)
    )

# OPTIMIZED LEAST SQUARES FIT FOR ALPHA AND BETA CAN BE DERIVED
# THROUGH CALCULUS OR ALGEBRA
def least_squares_fit(xs, ys):
    beta = correlation(xs, ys) * standard_deviation(ys) / standard_deviation(xs)
    alpha = mean(ys) - beta * mean(xs)
    return alpha, beta

trainer_alpha, trainer_beta = least_squares_fit(
    trainer_pokemon_counts, 
    trainer_win_counts
)

# print('trainer_alpha = %s' % trainer_alpha)
# print('trainer_beta = %s' % trainer_beta)
# print('linear model: number of wins = %s * number of pokemon + %s' % (trainer_beta, trainer_alpha))

def squared_mean_deviations(a_vector):
    list_mean = mean(a_vector)
    return map(lambda num: (num - list_mean) ** 2, a_vector)

def r_squared(alpha, beta, xs, ys):
    return 1 - (
        sum_of_squared_errors(alpha, beta, xs, ys) / sum(squared_mean_deviations(ys))
    )

trainer_r_squared = r_squared(trainer_alpha, trainer_beta, trainer_pokemon_counts, trainer_win_counts)

# print('trainer r^2 = %s' % trainer_r_squared)

# ON PAGE 249
