import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/12-exercises'
)
from data_split_for_model_training import split_data

from naive_bayes import NaiveBayesClassifier
from data_harvester import data
import random
import pdb
from collections import defaultdict

random.seed(0)
train_data, test_data = split_data(data, 0.75)
print("train_data_length = %s" % len(train_data))
print("test_data_length = %s" % len(test_data))

classifier = NaiveBayesClassifier()
# pdb.set_trace()
classifier.train(train_data)
classified = [
    (subject, is_spam, classifier.classify(subject))
    for subject, is_spam
    in test_data
]


true_positives = []
true_negatives = []
false_positives = []
false_negatives = []
subject, classification, predicted_prob = 0, 1, 2
for my_tuple in classified:
    is_spam = my_tuple[classification]
    predict_is_spam = (my_tuple[predicted_prob] > 0.5)
    # if predict_is_spam:
    #     print('hey ho!')
    # pdb.set_trace()
    if is_spam and predict_is_spam:
        true_positives.append(my_tuple[subject])
    elif not is_spam and not predict_is_spam:
        true_negatives.append(my_tuple[subject])
    elif is_spam and not predict_is_spam:
        false_negatives.append(my_tuple[subject])
    else:
        false_positives.append(my_tuple[subject])

print('true positive count = %s' % len(true_positives))
print('true negative count = %s' % len(true_negatives))
print('false positive count = %s' % len(false_positives))
print('false negative count = %s' % len(false_negatives))

print('first 3 true positives')
for subject in true_positives[0:3]:
    print('     %s' % subject)

print('first 3 true negatives')
for subject in true_negatives[0:3]:
    print('     %s' % subject)

print('first 3 false positives')
for subject in false_positives[0:3]:
    print('    %s' % subject)

print('first 3 false negatives')
for subject in false_negatives[0:3]:
    print('    %s' % subject)

