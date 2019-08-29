import random

def split_data(data, proportion_testing):
    testing, training = [], []
    for row in data:
        if random.random() < proportion_testing:
            testing.append(row)
        else:
            training.append(row)
    return testing, training

def test_train_split(x, y, proportion_testing):
    data = zip(x, y)
    train, test = split_data(data, 1 - proportion_testing)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

def model_accuracy(true_positive, true_negative, false_positive, false_negative):
    correct_predictions = true_positive + true_negative
    total_cases = correct_predictions + false_positive + false_negative
    return correct_predictions / total_cases

def model_precision(true_positive, true_negative, false_positive, false_negative):
    return true_positive / (true_positive + false_positive)

def model_recall(true_positive, true_negative, false_positive, false_negative):
    return true_positive / (true_positive + false_negative)


def f1_score(true_positive, true_negative, false_positive, false_negative):
    precision = model_precision(true_positive, true_negative, false_positive, false_negative)
    recall = model_recall(true_positive, true_negative, false_positive, false_negative)
    return 2 * precision * recall / (precision + recall)

# OUR LUKE IS FOR LIEKEMIA CASE
#              | leukemia | no leukemia | total
#     'Luke'   |    70    |    4930     | 5000
#   not 'Luke' | 13930    |  981070     | 995000
#     total    | 14000    |  986000     | 1000000


luke_is_for_leukemi = {
    'true_positive': 70,
    'false_positive': 4930,
    'false_negative': 13930,
    'true_negative': 981070
}

luke_model_accuracy = model_accuracy(
    luke_is_for_leukemi['true_positive'],
    luke_is_for_leukemi['true_negative'],
    luke_is_for_leukemi['false_positive'],
    luke_is_for_leukemi['false_negative']
)

luke_model_precision = model_precision(
    luke_is_for_leukemi['true_positive'],
    luke_is_for_leukemi['true_negative'],
    luke_is_for_leukemi['false_positive'],
    luke_is_for_leukemi['false_negative']
)

luke_model_recall = model_recall(
    luke_is_for_leukemi['true_positive'],
    luke_is_for_leukemi['true_negative'],
    luke_is_for_leukemi['false_positive'],
    luke_is_for_leukemi['false_negative']
)

luke_model_f1_score = f1_score(
    luke_is_for_leukemi['true_positive'],
    luke_is_for_leukemi['true_negative'],
    luke_is_for_leukemi['false_positive'],
    luke_is_for_leukemi['false_negative']
)

# print('luke model accuracy = %s' % luke_model_accuracy)
# print('luke model precision = %s' % luke_model_precision)
# print('luke model recall = %s' % luke_model_recall)
# print('luke model f1 score = %s' % luke_model_f1_score)
