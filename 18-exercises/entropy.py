import math
from collections import Counter

def entropy(class_probabilities):
    return sum(
        -probability * math.log(probability, 2)
        for probability
        in class_probabilities
        if probability
    )

# DATA WILL COME IN THE FORM (input, label)

def class_probabilities(labels):
    total_count = len(labels)
    return [
        count / total_count
        for count 
        in Counter(labels).values()
    ]

def data_entropy(labeled_data):
    labels = [ label for _, label in labeled_data ]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets): # subsets is a list of lists
    total_count = sum ( len(subset) for subset in subsets )
    return sum (
        data_entropy(subset) * len(subset) / total_count
        for subset 
        in subsets
    )
