import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/09-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/12-exercises'
)
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/15-exercises'
)
from matplotlib import pyplot
from my_list_vectors import dot_product
from stochastic_gradient_descent_two import maximize_stochastic
from maximize_utils import maximize_batch
from data_split_for_model_training import test_train_split
from trainer_data import trainer_stats, beat_game_stats, trainer_avg_levels, trainer_team_counts, beat_game_trainers, not_beat_game_trainers
from functools import partial
from logistic_function import logistic, logistic_log_likelihood, logistic_log_likelihood_i, logistic_log_gradient, logistic_log_gradient_i
import pdb
import random

# random.seed(0)
x_train, x_test, y_train, y_test = test_train_split(
    trainer_stats, 
    beat_game_stats, 
    0.33
)

# Want to maximize log likelihood on the training data
beta_0 = [ random.random() for _ in range(3) ]

beta_hat = maximize_stochastic(
    logistic_log_likelihood_i,
    logistic_log_gradient_i,
    x_train, 
    y_train,
    beta_0,
    0.0001
)

print('beta_hat = %s' % beta_hat)

# TEST GOODNESS OF FIT
# true_positives = true_negatives = false_positives = false_negatives = 0
# for x_i, y_i in zip(x_test, y_test):

#     dot_beta_x_i = dot_product(beta_hat, x_i)
#     prediction = logistic(dot_beta_x_i)

#     # print('dot(beta_hat, x_i) = %s' % dot_beta_x_i)
#     # print('logistic(dot_beta_x_i) = %s' % prediction)

#     if y_i == 1 and prediction > 0.6:
#         true_positives += 1
#     elif y_i == 1:
#         false_negatives += 1
#     elif y_i == 0 and prediction > 0.6:
#         false_positives += 1
#     else:
#         true_negatives += 1

# precision = true_positives / (true_positives + false_positives)
# recall = true_positives / (true_positives + false_negatives)
# print('precision = %s' % precision)
# print('recall = %s' % recall)

# A + beta_level * avg_level + beta_team_count * team_count = 0
# avg_level = -(a + beta_team_count * team_count) / beta_level
def classification_line_avg_level(beta_hat, team_count):
    beta_a = beta_hat[0]
    beta_level = beta_hat[1]
    beta_team_count = beta_hat[2]
    return -(beta_a + beta_team_count * team_count) / beta_level

classification_ys = [ 1, 2, 3, 4, 5, 6 ]
classification_xs = [
    classification_line_avg_level(beta_hat, team_count)
    for team_count
    in classification_ys
]


# VISUALIZE
beat_game_trainer_average_level = [
    trainer['party_average_level']
    for trainer
    in beat_game_trainers
]

beat_game_trainer_team_count = [
    trainer['team_count']
    for trainer
    in beat_game_trainers
]

not_beat_game_trainer_average_level = [
    trainer['party_average_level']
    for trainer
    in not_beat_game_trainers
]

not_beat_game_trainer_team_count = [
    trainer['team_count']
    for trainer
    in not_beat_game_trainers
]

pyplot.scatter(beat_game_trainer_average_level, beat_game_trainer_team_count, marker='^', label="beat game")
pyplot.scatter(not_beat_game_trainer_average_level, not_beat_game_trainer_team_count, marker='*', label="not beat game")
pyplot.scatter(classification_xs, classification_ys, marker='.', label="not beat game")
pyplot.xlabel('average level')
pyplot.ylabel('team count')
pyplot.legend()
pyplot.xlim(xmin=0, xmax=100)
pyplot.show()