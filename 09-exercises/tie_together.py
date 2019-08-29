from step_sizes import make_safe, step_sizes
import pdb

def step(vector, direction, step_size):
    return [
        vector_component + direction_i * step_size
        for vector_component, direction_i
        in zip(vector, direction)
    ]

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    # use gradient descent to find theta that minimizes target function
    theta = theta_0
    safe_target_fn = make_safe(target_fn)
    value = safe_target_fn(theta)

    while True:
        # pdb.set_trace()
        gradient = gradient_fn(theta)

        next_thetas = [
            step(theta, gradient, -step_size) for step_size in step_sizes
        ]

        next_theta = min(next_thetas, key=safe_target_fn)
        if safe_target_fn(next_theta) == float('inf'):
            pdb.set_trace()
        next_value = safe_target_fn(next_theta)
        print('next tolerance: %s' % (abs(value - next_value)))
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value
