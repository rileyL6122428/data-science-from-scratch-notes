import math
import sys

sys.path.append('07-exercises')
from prob import normal_cdf, invert_normal_cdf

normal_prob_below = normal_cdf

def normal_prob_above(x, mean, std_dev):
    return 1 - normal_cdf(x, mean, std_dev)

print('standard normal_prob_above 0: %s' % normal_prob_above(0, 0, 1))
print('standard normal_prob_above 1: %s' % normal_prob_above(1, 0, 1))

def normal_prob_between(hi, lo, mean, std_dev):
    return normal_cdf(hi, mean, std_dev) - normal_cdf(lo, mean, std_dev)

print('standard normal_prob_between -1 -> 1 = %s' % normal_prob_between(1, -1, 0, 1))

def normal_prob_outside(hi, lo, mean, std_dev):
    return normal_prob_below(lo, mean, std_dev) + normal_prob_above(hi, mean, std_dev)

print('standard normal_prob_outside -1 -> 1 = %s' % normal_prob_outside(1, -1, 0, 1))

# WRITE PRINT STATEMENTS TO ILLUSTRATE THE ABOVE!
# UP NEXT, FIND START OF TAIL REGIONS GIVEN PROBS

def normal_upper_bound(prob, mean, std_dev):
    return invert_normal_cdf(prob, mean, std_dev)

print('standard normal_upper_bound for .6 = %s' % normal_upper_bound(.6, 0, 1))


def normal_lower_bound(prob, mean, std_dev):
    return invert_normal_cdf(1 - prob, mean, std_dev)

print('standard normal_lower_bound 0.6 = %s' % normal_lower_bound(0.6, 0, 1))

def normal_two_sided_upper_bound_first_attempt(prob, mean=0, std_dev=1, tolerance=0.00001):
    if mean != 0 or std_dev != 1:
        return mean + std_dev * normal_two_sided_bound(prob, tolerance=tolerance)
    
    hi_half_z, hi_half_x = 0.5, 10
    lo_half_z, lo_half_x = 0, 0
    while hi_half_z - lo_half_z > tolerance:
        mid_half_x = (hi_half_x + lo_half_x) / 2
        mid_half_z = normal_cdf(mid_half_x, 0, 1) - 0.5
        if mid_half_z > prob / 2:
            hi_half_x, hi_half_z = mid_half_x, mid_half_z
        elif mid_half_z < prob / 2:
            lo_half_x, lo_half_z = mid_half_x, mid_half_z
        else:
            break

    return (hi_half_x + lo_half_x) / 2

print('standard normal_two_sided_upper_bound_first_attempt .68 = %s' % normal_two_sided_upper_bound_first_attempt(.68))


def normal_two_sided_bounds(prob, mean=0, std_dev=1):
    tail_prob = (1 - prob)/ 2
    lower_tail_bound = normal_upper_bound(tail_prob, mean, std_dev)
    upper_tail_bound = normal_lower_bound(tail_prob, mean, std_dev)
    return lower_tail_bound, upper_tail_bound
# print('standard normal_two_sided_upper_bound .68 = %s' % normal_two_sided_upper_bound(.68))



# Let's do some confidence testing
# We will test probs of a coin is fair 
# Our null Hyp H_0 = heads with prob 0.5
# Oour alternative Hyp H_1 = heads with prob 0.55

def normal_approximation_to_binomial(trial_count, success_rate):
    mean = trial_count * success_rate
    std_dev = math.sqrt(success_rate * (1 - success_rate) * trial_count)
    return mean, std_dev

expected_mean, expected_std_dev = normal_approximation_to_binomial(1000, .5)
print('expected mean for fair coin: %s' % expected_mean)
print('expected std_dev for fair coin: %s' % expected_std_dev)

# We will test with a 5% willingness to make a Type 1 Error
lower_bound, upper_bound = normal_two_sided_bounds(0.95, expected_mean, expected_std_dev)
print(
    'head totals for a 1000 trials are expected to have 95 percent between: [%s, %s]' % (lower_bound, upper_bound)
)

# Will will let our alternative Hyp be that p = .55, favor heads
alternative_mean, alternative_std_dev = normal_approximation_to_binomial(1000, .55)
print('alternative_mean = %s' % alternative_mean)
print('alternative_std_dev = %s' % alternative_std_dev)

# Type 2 probability is the change that we fail to reject the null hyp
# when our alternative hyp is preferable
type_2_probability = normal_prob_between(upper_bound, lower_bound, alternative_mean, alternative_std_dev)
print('type_2 prob = %s' % type_2_probability)

# POWER is the chance of not committing a type 2 error
power = 1 - type_2_probability 
print('POWER = %s' % power)
