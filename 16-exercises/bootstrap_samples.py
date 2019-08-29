import random

def bootstrap_sample(data):
    return [
        random.choice(data) for _ in data
    ]

def bootstrap_statistic(data, stats_function, num_sample):
    return [
        stats_function(bootstrap_sample(data))
        for _
        in range(num_sample)
    ]
    