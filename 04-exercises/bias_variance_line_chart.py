from matplotlib import pyplot

variance_by_complexity = [1, 2, 4, 8,  16, 32, 64, 128, 256]
bias_squared_by_complexity = list(reversed(variance_by_complexity))
total_error_by_complexity = [
    variance + bias_squared 
    for variance, bias_squared
    in zip(variance_by_complexity, bias_squared_by_complexity)
]

x_coords = [ index for index, _ in enumerate(variance_by_complexity)]

pyplot.plot(x_coords, variance_by_complexity, 'g-', label='variance')
pyplot.plot(x_coords, bias_squared_by_complexity, 'r-', label='bias^2')
pyplot.plot(x_coords, total_error_by_complexity, 'b:', label='total error')

pyplot.legend(loc=9) # loc is location top center
pyplot.xlabel('model complexity')
pyplot.title('The Bias-Variance Tradeoff')
pyplot.show()