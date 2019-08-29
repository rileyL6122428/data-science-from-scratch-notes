from math import exp, sqrt, pi, erf
import random

def uniform_prob_density_func(x):
    return 1 if x >= 0 and x <= 1 else 0

def uniform_cdf(x):
    if x < 0: 
        return 0
    elif x < 1:
        return x
    else:
        return 1

def normal_prob_dist_func(x, mu=0, std_dev=1):
    return exp((-1 * (x - mu) ** 2)/ (2 * std_dev ** 2)) / (sqrt(2 * pi) * std_dev)

def normal_cdf(x, mean=0, std_dev=1):
    return (1 + erf( (x - mean) / (sqrt(2) * std_dev) ) ) / 2

def invert_normal_cdf(cumulative_prob, mean=0, std_dev=1, tolerance=0.00001):
    if mean != 0 or std_dev != 1:
        return mean + std_dev * invert_normal_cdf(cumulative_prob, tolerance=tolerance)
    
    low_z, low_cumulative_prob = -10.0, 0
    high_z, high_cumulative_prob = 10.0, 1

    while high_z - low_z > tolerance:
        mid_z = (high_z + low_z) / 2
        mid_cumulative_prob = normal_cdf(mid_z)
        if mid_cumulative_prob > cumulative_prob:
            high_z, high_cumulative_prob = mid_z, mid_cumulative_prob
        elif mid_cumulative_prob < cumulative_prob:
            low_z, low_cumulative_prob = mid_z, mid_cumulative_prob
        else:
            break
    return (high_z + low_z) / 2

def bernoulli_trial(prob):
    return 1 if random.random() < prob else 0

def binomial_random_var(trial_total, trial_probability):
    return sum(bernoulli_trial(trial_probability) for _ in range(trial_total))

# print('uniform pdf at 0.5 = %s' % uniform_prob_density_func(0.5))
# print('uniform pdf at 1.1 = %s' % uniform_prob_density_func(1.1))

# print('uniform cdf at -.2 = %s' % uniform_cdf(-0.2))
# print('uniform cdf at 0.4 = %s' % uniform_cdf(0.4))
# print('uniform cdf at 1.1 = %s' % uniform_cdf(1.1))

# print('normal(x=0, mu=0, std_dev=1) = %s' % normal_prod_dist_func(0))
# print('normal(x=0.4, mu=0, std_dev=1) = %s' % normal_prod_dist_func(0.4))
# print('normal(x=1.1, mu=0, std_dev=1) = %s' % normal_prod_dist_func(1.1))

# print('invert normal cdf(.5, mu=0, std_dev=1) = %s' % invert_normal_cdf(.5))
# print('invert normal cdf(.2, mu=0, std_dev=1) = %s' % invert_normal_cdf(.2))

# print('bernoulli trial(0.6) = %s' % bernoulli_trial(0.6))
# print('binomail_random_var(5, .8) = %s' % binomial_random_var(5, .8))
