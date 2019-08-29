import random
import pdb
# USUALLY, ERROR FUNCTIONS FOR GRADIENT DESCENT PROBLEMS ARE ADDITIVE
# WHICH MEANS THE PREDICTIVE ERROR ON THE WHOLE DATA SET IS SIMPLY THE SUM
# OF THE PREDICTIVE ERRORS FOR EACH DATA POINT

# STOCHASTIC GRADIENT DESCENT:
# COMPUTES THE GRADIENT OF A SINGLE DATA POINT AND TAKES A STEP
# IT CYCLES OVER OUR DATA REPEATEDLY UNTIL IT REACHES A STOPPING POINT

def random_order(data):
    indexes = [ index for index, _ in enumerate(data) ]
    random.shuffle(indexes)
    for index in indexes:
        yield data[index]


def vector_subtract(vector_a, vector_b):
    return [
        component_a - component_b
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

def scalar_multiply(scalar, vector):
    return [
        scalar * component
        for component
        in vector
    ]

def minimize_stochastic(target_fn, gradient_fn, xs, ys, theta_0, alpha_0=0.01):
    data = list(zip(xs, ys))
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    iterations_with_no_improvement = 0
    print('theta_0 = %s' % theta_0)

    while iterations_with_no_improvement < 100:
        value = sum( 
            target_fn(x_i, y_i, theta) 
            for x_i, y_i 
            in data 
        )

        if value < min_value:
            print('next_theta = %s' % theta)
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            print('iterations_with_no_improvement = %s' % iterations_with_no_improvement)
            alpha *= 0.9

        for x_i, y_i in random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta

def negate(func):
    return lambda *args, **kwargs : -func(*args, **kwargs)

def negate_all(func):
    return lambda *args, **kwargs : [ -y for y in func(*args, **kwargs) ]

def maximize_stochastic(target_func, gradient_func, x, y, theta_0, tolerance=0.01):
    return minimize_stochastic(
        negate(target_func),
        negate_all(gradient_func),
        x, y,
        theta_0,
        tolerance
    )

# TEST STOCHASTIC GRADIENT DESCENT
from simple_linear_regression import error
from pokemon_trainer_data import trainer_pokemon_counts, trainer_win_counts

def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i)

def squared_error_gradient(x_i, y_i, theta):
    alpha, beta, = theta
    return [
        -2 * error(alpha, beta, x_i, y_i),      # alpha partial derivative
        -2 * error(alpha, beta, x_i, y_i) * x_i # beta partial derivative
    ]

# theta = [ random.random() - 0.5, random.random() - 0.5 ]

# alpha, beta = minimize_stochastic(
#     squared_error,
#     squared_error_gradient,
#     trainer_pokemon_counts,
#     trainer_win_counts,
#     theta,
#     0.001
# )

# print('stochastic alpha = %s' % alpha)
# print('stochastic beta = %s' % beta)