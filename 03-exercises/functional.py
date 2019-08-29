# can curry with partial function
from functools import partial, reduce

def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)

print('2 to the 5th power = %s' % two_to_the(5))

# can also use parital for later args, if parameter names specified
squared = partial(exp, power=2)
print('9 squared = %s' % squared(9))

# map, reduce, and filter provide nice alternatives to list comprehensions
def double(num):
    return num * 2

my_vals = [1, 2, 3, 4]
print('my_vals = %s' % my_vals)

my_vals_doubled = [double(num) for num in my_vals]
print('my_vals_doubled = %s' % my_vals_doubled)

my_vals_doubled_by_map = map(double, my_vals)
print('my_vals_doubled_by_map = %s' % my_vals_doubled)

list_doubler = partial(map, double)
my_vals_doubled_by_list_doubler = list(list_doubler(my_vals))
print('my_vals_doubled_by_list_doubler = %s' % my_vals_doubled_by_list_doubler)

# filter does work of 'if' list comprehension
def is_even(num):
    return num % 2 == 0

my_even_vals = [num for num in my_vals if is_even(num)]
print('my_even_vals = %s' % my_even_vals)

my_even_vals_by_filter = list(filter(is_even, my_vals))
print('my_even_vals_by_filter = %s' % my_even_vals_by_filter)

# reduce is cool
def product(num_a, num_b):
    return num_a * num_b

my_product = reduce(product, my_vals)
print('my_product = %s' % my_product)

