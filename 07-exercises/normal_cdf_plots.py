from prob import normal_cdf
from matplotlib import pyplot

x_vals = [ num / 10 for num in range(-50, 50) ]

pyplot.plot(x_vals, [ normal_cdf(x_val) for x_val in x_vals ], '-', label='mu=0;std_dev=1')
pyplot.plot(x_vals, [ normal_cdf(x_val, std_dev=.5) for x_val in x_vals ], '--', label='mu=0;std_dev=.5')
pyplot.plot(x_vals, [ normal_cdf(x_val, std_dev=2) for x_val in x_vals ], ':', label='mu=0;std_dev=2')
pyplot.plot(x_vals, [ normal_cdf(x_val, mean=1) for x_val in x_vals ], '-.', label='mu=1;std_dev=1')
pyplot.legend()
pyplot.title('Various Normal CDFs')
pyplot.show()
