# import pdb

step_sizes = [ 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001 ]

def make_safe(function):
    def safe_function(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            return float('inf')
    return safe_function

