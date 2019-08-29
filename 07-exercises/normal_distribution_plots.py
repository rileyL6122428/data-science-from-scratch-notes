from matplotlib import pyplot
from prob import normal_prob_dist_func

x_vals = [ num / 10 for num in range(-50, 50) ]
pyplot.plot(x_vals, [normal_prob_dist_func(x=num) for num in x_vals], '-', label='mu=0, std_dev=1')
pyplot.plot(x_vals, [normal_prob_dist_func(num, std_dev=2) for num in x_vals], '-', label='mu=0, std_dev=2')
pyplot.plot(x_vals, [normal_prob_dist_func(num, std_dev=.5) for num in x_vals], '-', label='mu=0, std_dev=.5')
pyplot.plot(x_vals, [normal_prob_dist_func(num, mu=-1) for num in x_vals], '-', label='mu=-1, std_dev=1')
pyplot.title('Various Normal Distributions')
pyplot.legend()
pyplot.show()