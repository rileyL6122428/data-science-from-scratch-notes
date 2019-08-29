from math import gamma
from matplotlib import pyplot

# beta_distribution used for normalization of the beta prob dist function (pdf)
def beta_distribution(alpha, beta):
    return gamma(alpha) * gamma(beta) / gamma(alpha + beta)

# print('beta_dist(0.5, 0.5) = %s' % beta_distribution(.5, .5))
# print('beta_dist(2, 1) = %s' % beta_distribution(2, 1))
# print('beta_dist(2, 3) = %s' % beta_distribution(2, 3))

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0
    return (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / beta_distribution(alpha, beta)

# print('beta_pdf(.5, 1, 1) = %s' % beta_pdf(.5, 1, 1))

# Generally speaking distribution centers weight at 
# alpha / (alpha + beta)

# Draw example beta distributions
# x_vals = [ num / 100 for num in range(100) ]
# beta_1_1 = [ beta_pdf(x_val, 1, 1) for x_val in x_vals ]
# beta_10_10 = [ beta_pdf(x_val, 10, 10) for x_val in x_vals ]
# beta_4_16 = [ beta_pdf(x_val, 4, 16) for x_val in x_vals ]
# beta_16_4 = [ beta_pdf(x_val, 16, 4) for x_val in x_vals ]

# pyplot.plot(x_vals, beta_1_1, color='green', label='beta_1_1')
# pyplot.plot(x_vals, beta_10_10, color='red', label='beta_10_10')
# pyplot.plot(x_vals, beta_4_16, color='orange', label='beta_4_16')
# pyplot.plot(x_vals, beta_16_4, color='purple', label='beta_16_4')

# pyplot.legend()
# pyplot.show()
