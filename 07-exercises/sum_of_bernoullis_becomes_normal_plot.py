from prob import binomial_random_var
from matplotlib import pyplot
from collections import Counter

def make_bernoulli_histogram(success_prob, trial_count, binomial_var_total):
    outcomes = [ 
        binomial_random_var(trial_count, success_prob) 
        for _ 
        in range(binomial_var_total) 
    ]

    outcome_counts = Counter(outcomes)
    pyplot.bar(
        [ outcome for outcome in outcome_counts.keys() ],
        [ outcome_count for outcome_count in outcome_counts.values() ],
        0.8,
        color='0.75'
    )
    pyplot.title('Sum of many bernoullis approaches normal dist with large')
    pyplot.show()

make_bernoulli_histogram(0.6, 60, 100000)
    
