import re
import pdb
import math
from collections import defaultdict

training_set = [
    ('Hey, this is Chad, message me when you\'re free', False),
    ('Win a free subscription of Viagra', True),
    ('Last chance to win free Viagra', True),
    ('Want a free authentic authentic Rolex', True),
    ('Great job at the code convention', False),
    ('Job offer', False)
]


def tokenize(message):
    message_lowered = message.lower()
    words = re.findall("[a-z0-9']+", message_lowered)
    return set(words)
# test_words = 'All the words, all the time'
# print('tokenize("%s") = %s' %(test_words, tokenize(test_words)))

def count_words(training_set):
    # training instance looks like (message, is_spam)
    counts = defaultdict(lambda: { "is_spam": 0, "not_spam": 0 })
    for (message, is_spam) in training_set:
        for word in tokenize(message):
            counts[word]["is_spam" if is_spam else "not_spam"] += 1
    return counts
# print('count_words(training_set) = %s' % count_words(training_set))

def word_probabilities(counts, total_spams, total_not_spams, k=0.5):
    return [
        { 
            "word": word, 
            "word | is_spam": (counts[word]['is_spam'] + k) / (2 * k + total_spams),
            "word | !is_spam": (counts[word]['not_spam'] + k) / (2 * k + total_not_spams)
        }
        for word
        in counts.keys()
    ]
# counted_words = count_words(training_set)
# print('word_probabilities(counted_words, 2, 2) = %s' % word_probabilities(counted_words, 2, 2))

def spam_probability(word_probs, message):
    message_words = tokenize(message)
    logarithmic_prob_of_message_if_spam = 0.0
    logarithmic_prob_of_message_if_not_spam = 0.0

    for word_prob in word_probs:
        word = word_prob['word']
        word_prob_given_is_spam = word_prob['word | is_spam']
        word_prob_given_is_not_spam = word_prob['word | !is_spam']

        if word in message_words:
            logarithmic_prob_of_message_if_spam += math.log(word_prob_given_is_spam)
            logarithmic_prob_of_message_if_not_spam += math.log(word_prob_given_is_not_spam)

        else:
            logarithmic_prob_of_message_if_spam += math.log(1 - word_prob_given_is_spam)
            logarithmic_prob_of_message_if_not_spam += math.log(1 - word_prob_given_is_not_spam)

    message_prob_if_spam = math.exp(logarithmic_prob_of_message_if_spam)
    message_prob_if_not_spam = math.exp(
        logarithmic_prob_of_message_if_not_spam
    )
    return message_prob_if_spam / (
        message_prob_if_spam + message_prob_if_not_spam
    )


# my_word_probabilities = word_probabilities(counted_words, 3, 3)

# my_not_spam_message = 'Chad'
# print('spam_probability(my_word_probabilities, my_not_spam_message) = %s' % (
#     spam_probability(my_word_probabilities, my_not_spam_message)
# ))

# my_spam_message = 'Congratulations! You win a free Viagra!'
# print('spam_probability(my_word_probabilities, my_spam_message) = %s' % (
#     spam_probability(my_word_probabilities, my_spam_message)
# ))

# ON PAGE 240

class NaiveBayesClassifier:
    
    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []
    
    def train(self, training_set):
        num_spams = len([
            is_spam
            for message, is_spam in training_set
            if is_spam
        ])
        num_not_spams = len(training_set) - num_spams

        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(
            word_counts,
            num_spams,
            num_not_spams,
            self.k
        )
    
    def classify(self, message):
        return spam_probability(self.word_probs, message)
