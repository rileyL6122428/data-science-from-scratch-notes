from tie_together import minimize_batch
from functools import reduce
import random

def sum_of_squares(vector):
    return reduce(lambda accum, next: accum + next ** 2, vector, 0)

def sum_of_squares_gradient(vector):
    return [ 2 * vect_component for vect_component in vector ]

theta_0 = [ random.randint(-10, 10) for _ in range(3) ]

theta_final = minimize_batch(
    sum_of_squares,
    sum_of_squares_gradient,
    theta_0    
)

print('theta_0 = %s' % theta_0)
print('sum_of_squares(theta_0) = %s' % sum_of_squares(theta_0))
print('theta_final = %s' % theta_final)
print('sum_of_squares(theta_final) = %s' % sum_of_squares(theta_final))
