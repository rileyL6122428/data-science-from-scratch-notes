# At DataSciencester, we are trying to get people to click on an ad for
# an energy drink.
# We try with Banner A = "Tastes Great!"
# and Banner B = "Less Bias!"

# if n_A is number clicking ad A and N_A is total number viewed
# then n_A / N_A is a bernoulli random var (similar for B)
import math
from fair_coin_hyp_testing import normal_prob_above, normal_prob_below

def two_sided_p_value(x, mean=0, std_dev=1):
    if x > mean:
        return 2 * normal_prob_above(x, mean, std_dev)
    else:
        return 2 * normal_prob_below(x, mean, std_dev)

def estimated_mean(total_viewers, total_ad_clickers):
    p_hat = total_ad_clickers / total_viewers
    mean = p_hat
    return mean

def estimated_std_dev(total_viewers, total_ad_clickers):
    p_hat = total_ad_clickers / total_viewers
    return math.sqrt((p_hat) * (1 - p_hat) / total_viewers)

# If a and b are normal and independant, then the difference of 
# a and b ought to normal with
# mean = p_b - p_a
# std_dev = sqrt(var(a) + var(b))

# We will form a null hypothesis that A & B are roughly equal, or that
# p_b - p_a ≈ 0
# a_b_test_stat should be STANDARD normal:
def a_b_test_stat(a_trial_count, a_success_count, b_trial_count, b_success_count):
    a_mean = estimated_mean(a_trial_count, a_success_count)
    a_std_dev = estimated_std_dev(a_trial_count, a_success_count)
    b_mean = estimated_mean(b_trial_count, b_success_count)
    b_std_dev = estimated_std_dev(b_trial_count, b_success_count)
    return (b_mean - a_mean) / math.sqrt(a_std_dev ** 2 + b_std_dev ** 2)

z = a_b_test_stat(1000, 200, 1000, 180)
print('z = %s' % z)
print('two_sided_p_value = %s' % two_sided_p_value(z, 0, 1)) 
# On page 138