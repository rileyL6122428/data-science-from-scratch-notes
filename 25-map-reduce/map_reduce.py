from functools import partial
from collections import defaultdict

def map_reduce(inputs, mapper, reducer):
    collector = defaultdict(list)

    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)
    
    return [
        output
        for key, values in collector.items()
        for output in reducer(key, values)
    ]

def reduce_values_using(aggregation_fn, key, values):
    yield (key, aggregation_fn(values))

def values_reducer(aggregation_fn):
    return partial(
        reduce_values_using,
        aggregation_fn
    )

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer( lambda values: len(set(values)) )
    