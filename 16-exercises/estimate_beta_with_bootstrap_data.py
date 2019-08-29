import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/06-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/07-exercises'
)
from dispersion import standard_deviation
from multiple_regression import estimate_beta, trainer_beta
from bootstrap_samples import bootstrap_statistic
from pokemon_trainers import trainer_party_stats, trainer_badge_counts
from prob import normal_cdf
import random

def estimate_sample_beta(sample):
    x_sample, y_sample = zip(*sample)
    return estimate_beta(x_sample, y_sample)


# Repeatedly take a bootstrap sample
# If coefficient of one of the indpendent vars doesn't vary much across samples,
# then we can be confident that our estimate is relatively tight.
# If the coefficient varies greatly across samples, then we can't be at all
# confident in our estimate.
random.seed(0)
bootstrap_betas = bootstrap_statistic(
    list(zip(trainer_party_stats, trainer_badge_counts)),
    estimate_sample_beta,
    10
)

print('bootstrap betas:')
for beta in bootstrap_betas:
    print('beta = %s' % beta)

bootstrap_standard_errors = [
    standard_deviation([ 
        beta[index] 
        for beta 
        in bootstrap_betas
    ])
    for index 
    in range(3)
]

print('standard errors: %s' % bootstrap_standard_errors)

# We can then evaluate the meaningfulness of the betas 
# with the following calculations
def p_value(beta_hat_j, sigma_hat_j):
    if beta_hat_j > 0:
        return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
    else:
        return 2 * normal_cdf(beta_hat_j / sigma_hat_j)

actual_beta = trainer_beta

p_values = [
    p_value(trainer_beta_component, bootstrap_error_component)
    for trainer_beta_component , bootstrap_error_component
    in zip(actual_beta, bootstrap_standard_errors)
]

print('actual_beta: %s' % actual_beta)

print('p values: %s' % p_values)
# In this case, average level tends to be a good predictor of badge counts,
# because it's p value is close to zero. alpha and number of pokemon types in 
# party are appreciably larger than 0, suggesting they are not reliable 
# indicators in this model
