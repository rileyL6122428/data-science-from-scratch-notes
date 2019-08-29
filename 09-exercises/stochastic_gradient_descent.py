import random
from maximize_utils import negate, negate_all

def vector_subtract(vector_a, vector_b):
    return [ 
        component_a - component_b
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

def scalar_multiply(num, vector):
    return [ num * component for component in vector ]

def random_order(data):
    indexes = list(range(len(data)))
    random.shuffle(indexes)
    for index in indexes:
        yield data[index]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = list(zip(x, y))
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    iterations_with_no_improvement = 0

    while iterations_with_no_improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        if value < min_value: # we are moving towards the minimized solution
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9
        
        for x_i, y_i in random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
        
    return min_theta
            
def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(
        negate(target_fn),
        negate_all(gradient_fn),
        x,
        y,
        theta_0,
        alpha_0
    )