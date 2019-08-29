from functools import reduce
from matplotlib import pyplot

def sum_of_squares(vector):
    return reduce(lambda cumulative, next: cumulative + next ** 2, vector)

print('sum of sqaures([1, 2]) = %s' % sum_of_squares([1, 2]))

# gradient is the vector of partial derivative
# gives the input direction in which the function most quickly increases
# opposite direction of gradient minimizes

# derivative of single var function f at x is the limit of difference quotient
# as h -> 0
# geometrically represented as the slope of the tangent line a (x, f(x))
def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(num):
    return num ** 2

def square_prime(num):
    return 2 * num

# We can use difference quotients to approximate single var gradients
# for functions whose derivatives ain't easy to compute
# x_vals = [ num for num in range(-10, 10) ]
# square_primes = [ square_prime(x) for x in x_vals ]
# approx_square_primes = [ difference_quotient(square, x, 0.00001) for x in x_vals ]

# pyplot.plot(x_vals, square_primes, 'rx', label='Actual')
# pyplot.plot(x_vals, approx_square_primes, 'b+', label='Approximate')
# pyplot.legend()
# pyplot.show()

# When f is a function of many variables, it has multiple partial derivatives

def partial_difference_quotient(f, vector, i, h):
    # compute the i'th partial difference quotient of f at v
    w = [
        v_j + (h if j == i else 0)
        for j, v_j
        in enumerate(vector)
    ]
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [
        partial_difference_quotien(f, v, i, h)
        for i, _
        in enumerate(v)
    ]
