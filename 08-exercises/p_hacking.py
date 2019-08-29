# continuing with fair coin experiement
# for 1000 flips, we expect to see total number of heads
# between 469 & 531 based on 95% prob bounds of 
# adjusted normal curve
import random

def run_experiment():
    # flip fair coin 1000 times, true = head, false = tails
    return [ random.random() < .5 for _ in range(1000) ]

def reject_fairness(experiment):
    number_of_heads = len([outcome for outcome in experiment if outcome])
    return number_of_heads < 469 or number_of_heads > 531

def rejections(total_experiments):
    experiments = [run_experiment() for _ in range(total_experiments)]
    return len([experiment for experiment in experiments if reject_fairness(experiment)])

print('rejections from 1000 experiements: %s' % rejections(1000))